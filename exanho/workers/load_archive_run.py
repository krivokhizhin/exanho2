import concurrent.futures
import io
import logging
import datetime
import time
import zipfile

from collections import namedtuple
from multiprocessing import shared_memory
from ftplib import FTP

import exanho.eis44.config as config
import exanho.orm.sqlalchemy as domain

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
    now = datetime.datetime.now()

    while True:
        futures = set()
        with domain.session_scope() as session:
            # ready_archives = session.query(LoadArchive).filter(LoadArchive.status == ArchiveStatus.READY)
            for load_archive in session.query(LoadArchive).filter(LoadArchive.status == ArchiveStatus.READY).order_by(LoadArchive.date).limit(config.load_archive_max_workers):
                log.debug(load_archive)
                load_archive.status = ArchiveStatus.LOADING
                session.flush()
                future = executor.submit(ftp_loading, config.ftp_host, config.ftp_port, config.ftp_user, config.ftp_password, load_archive.id, load_archive.name, load_archive.task.location)
                futures.add(future)
        
        wait_for(futures)

        with domain.session_scope() as session:
            if session.query(LoadArchive).filter(LoadArchive.status == ArchiveStatus.READY).count() == 0:
                break

    log.info(f'work')

def finalize():
    executor.shutdown(True)

    log.info(f'finalize')

def ftp_loading(host, port, user, password, load_archive_id, archivename, location):
    log = logging.getLogger(__name__)

    files = []

    with FTP() as ftp_client:
    
        ftp_client.connect(host, port)
        ftp_client.login(user, password)            
        ftp_client.cwd(location) 

        for filename, crc, size, last_modify in download_extract_zip(ftp_client, archivename):                
            log.debug((filename, crc, size, last_modify))
            files.append(FileData(filename, crc, size, last_modify, filename))

    return (load_archive_id, files)


def download_extract_zip(ftp_client, zipfilename, ext_file='.xml'):
    """
    Download a ZIP file from FTP and extract its contents in memory
    yields (filename, file-like object) pairs
    """
    with io.BytesIO() as buffer:
        
        try:
            ftp_client.retrbinary('RETR '+zipfilename, buffer.write)
        except Exception as ex:
            logger.exception('{}: ftp_client.retrbinary(RETR {}, buffer.write)'.format(ftp_client.pwd(), zipfilename), ex.args)
            raise
            
        with zipfile.ZipFile(buffer) as thezip:
            for zipinfo in thezip.infolist():
                
                if not zipinfo.filename.endswith(ext_file):
                    continue

                yield zipinfo.filename, zipinfo.CRC, zipinfo.file_size, datetime.datetime(*zipinfo.date_time)
                
                # with thezip.open(zipinfo) as thefile:
                #     yield zipinfo.filename, zipinfo.CRC, zipinfo.file_size, thefile.read()

def wait_for(futures):
    for future in concurrent.futures.as_completed(futures):
        err = future.exception()
        if err is None:
            load_archeve_id, files = future.result()                
            with domain.session_scope() as session:
                reassigned = 0                
                for file_data in files:
                    exists_file = session.query(LoadFile).\
                        filter(LoadFile.archive_id == load_archeve_id).\
                            filter(LoadFile.filename == file_data.filename).\
                                one_or_none()
                    if exists_file is None:
                        session.add(LoadFile(archive_id=load_archeve_id, status=FileStatus.CONSIDERED, filename=file_data.filename, crc=file_data.crc, size=file_data.size, last_modify=file_data.last_modify, message=file_data.message))
                    elif (exists_file.crc != file_data.crc) and (exists_file.last_modify < file_data.last_modify):
                        exists_file.crc = file_data.crc
                        exists_file.size = file_data.size
                        exists_file.last_modify = file_data.last_modify
                        exists_file.message = file_data.message
                        exists_file.status = FileStatus.CONSIDERED
                        reassigned += 1

                if session.new or reassigned:
                    log.info(f'Files: added {len(session.new)}, reassigned {reassigned}')
        else:
            pass