import array
import concurrent.futures
import io
import logging
import datetime
import time
import zipfile

from collections import namedtuple, defaultdict
from multiprocessing import shared_memory
from ftplib import FTP

import exanho.eis44.config as config
import exanho.orm.sqlalchemy as domain

from exanho.core.common import Error
from exanho.model.loading import TaskStatus, LoadTask, ArchiveStatus, LoadArchive, FileStatus, LoadFile

log = logging.getLogger(__name__)

FileData = namedtuple('FileData', ['filename', 'crc', 'size', 'last_modify', 'message'])
executor = concurrent.futures.ThreadPoolExecutor(config.load_archive_max_workers)

def initialize(*args, **kwargs):
    db_url = kwargs.get('db_url', None)
    if db_url:
        db_validate = kwargs.get('db_validate', False)
        if db_validate:
            is_valid, errors, warnings = domain.validate(db_url)
            if not is_valid:
                log.error(errors)
                if warnings:
                    log.warning(warnings)
                raise RuntimeError(f'The database schema does not match the ORM model')
            
        domain.configure(db_url)

    log.info(f'initialize')

def work():
    while True:
        futures = set()
        with domain.session_scope() as session:
            for load_archive in session.query(LoadArchive).filter(LoadArchive.status == ArchiveStatus.READY).order_by(LoadArchive.date).limit(config.load_archive_max_workers):
                load_archive.status = ArchiveStatus.LOADING
                future = executor.submit(ftp_loading, config.ftp_host, config.ftp_port, config.ftp_user, config.ftp_password, load_archive.id, load_archive.name, load_archive.task.location)
                futures.add(future)
                log.info(f'load_archive({load_archive.id}): {load_archive.status}')

            session.flush()

            file_statuses = session.query(LoadFile.archive_id, LoadFile.status).\
                filter(LoadFile.archive_id.in_(session.query(LoadArchive.id).filter(LoadArchive.status == ArchiveStatus.LOADING))).all()
            statuses_by_archive = defaultdict(list)
            for archive_id, file_status in file_statuses:
                statuses_by_archive[archive_id].append(file_status)

            for archive_id, statuses in statuses_by_archive.items():
                statuses_set = set(statuses)
                if (len(statuses_set) == 1) and (FileStatus.COMPLETE in statuses_set):
                    complete_archive = session.query(LoadArchive).get(archive_id)
                    complete_archive.status = ArchiveStatus.PERFORMED
                    complete_archive.err_desc = None
                    log.info(f'load_archive({complete_archive.id}): {complete_archive.status}')
                elif FileStatus.FAULT in statuses_set:
                    complete_archive = session.query(LoadArchive).get(archive_id)
                    complete_archive.status = ArchiveStatus.FAILED
                    complete_archive.err_desc = f'{statuses.count(ArchiveStatus.FAILED)} files have failed status'
                    log.info(f'load_archive({complete_archive.id}): {complete_archive.status}')

        if futures:
            wait_for(futures)

        with domain.session_scope() as session:
            if session.query(LoadArchive).filter(LoadArchive.status == ArchiveStatus.READY).count() == 0:
                break   

def finalize():
    executor.shutdown(True)
    log.info(f'finalize')

def ftp_loading(host, port, user, password, load_archive_id, archivename, location):
    try:
        files = []
        with FTP() as ftp_client:
        
            ftp_client.connect(host, port)
            ftp_client.login(user, password)            
            ftp_client.cwd(location) 

            for filename, crc, size, last_modify, message in download_extract_zip(ftp_client, archivename):
                files.append(FileData(filename, crc, size, last_modify, message))

        return (load_archive_id, archivename, location, files)
    except Exception as ex:
        log.exception(ex)
        raise Error(ex.args[0], ex, (load_archive_id, archivename, location))

def download_extract_zip(ftp_client, zipfilename, ext_file='.xml'):
    """
    Download a ZIP file from FTP and extract its contents in memory
    yields (filename, file-like object) pairs
    """
    with io.BytesIO() as buffer:
        
        ftp_client.retrbinary('RETR '+zipfilename, buffer.write)
            
        with zipfile.ZipFile(buffer) as thezip:
            for zipinfo in thezip.infolist():
                
                if not zipinfo.filename.endswith(ext_file):
                    continue

                shm = shared_memory.SharedMemory(create=True, size=zipinfo.file_size)
                message = shm.name              
                with thezip.open(zipinfo) as thefile:
                    shm.buf[:zipinfo.file_size] = thefile.read()
                shm.close()
                
                yield zipinfo.filename, zipinfo.CRC, zipinfo.file_size, datetime.datetime(*zipinfo.date_time), message

def wait_for(futures):
    for future in concurrent.futures.as_completed(futures):
        err = future.exception()
        if err is None:
            load_archeve_id, archivename, location, files = future.result()                
            with domain.session_scope() as session:
                reassigned = 0                
                for file_data in files:
                    exists_file = session.query(LoadFile).\
                        filter(LoadFile.archive_id == load_archeve_id).\
                            filter(LoadFile.filename == file_data.filename).\
                                one_or_none()
                    if exists_file is None:
                        session.add(LoadFile(archive_id=load_archeve_id, status=FileStatus.PREPARED, filename=file_data.filename, crc=file_data.crc, size=file_data.size, last_modify=file_data.last_modify, message=file_data.message))
                    elif (exists_file in [FileStatus.COMPLETE, FileStatus.FAULT, FileStatus.PREPARED]) and (exists_file.crc != file_data.crc) and (exists_file.last_modify < file_data.last_modify):
                        exists_file.crc = file_data.crc
                        exists_file.size = file_data.size
                        exists_file.last_modify = file_data.last_modify
                        exists_file.message = file_data.message
                        exists_file.status = FileStatus.PREPARED
                        reassigned += 1

                if session.new or reassigned:
                    log.info(f'{archivename} (id={load_archeve_id}): added {len(session.new)}, reassigned {reassigned} files')
        elif isinstance(err, Error):
            load_archive_id, archivename, location = err.params
            with domain.session_scope() as session:
                load_archive = session.query(LoadArchive).get(load_archive_id)
                if load_archive:
                    load_archive.status = ArchiveStatus.FAILED
                    load_archive.err_desc = err.message
                    log.error(f'{archivename} (id={load_archive_id}) error')
        else:
            raise err