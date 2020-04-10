import io
import logging
import datetime
import time
import zipfile

from collections import namedtuple
from ftplib import FTP
from threading import Thread
from queue import Queue

import exanho.eis44.config as config
import exanho.orm.sqlalchemy as domain

from exanho.model.loading import LoadStatus, LoadTask, LoadArchive, LoadFile
from exanho.eis44.ftp_extractor import FtpExtractor

log = logging.getLogger(__name__)

TaskExec = namedtuple('TaskExec', ['id', 'location'])
archive_queue = Queue(config.queue_max_size)
threads = []

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

    for i in range(config.num_loader_threads):
        t = Thread(target=ftp_loading, args=(config.ftp_host, config.ftp_port, config.ftp_user, config.ftp_password, archive_queue))
        t.daemon = True
        t.start()
        threads.append(t)

    log.info(f'initialize')

def work():  
    task = None  
    now = datetime.datetime.now()

    with domain.session_scope() as session:
        load_task = session.query(LoadTask).filter(LoadTask.scheduled_date < now).filter(LoadTask.status == LoadStatus.NEW.value).first()
        log.debug(load_task)
        if load_task:
            task = TaskExec(load_task.id, load_task.location)
            load_task.status = LoadStatus.EXECUTION.value

    if task is None:
        return

    extractor = FtpExtractor(host=config.ftp_host, port=config.ftp_port, user=config.ftp_user, password=config.ftp_password, location=task.location, archive_queue=archive_queue)
    extractor.extract()

    archive_queue.join()

    with domain.session_scope() as session:
        load_task = session.query(LoadTask).filter_by(id=task.id).one()
        load_task.status = LoadStatus.COMPLETE.value

    log.info(f'work')

def finalize():
    archive_queue.put(None)
    for t in threads:
        t.join()

    log.info(f'finalize')

def ftp_loading(host, port, user, password, archive_q):
    log = logging.getLogger(__name__)
    while True:
        archive = archive_q.get()
        if archive is None:
            archive_q.put(None)
            break

        location, archivename = archive

        archive_id = None

        with domain.session_scope() as session:
            load_archive = LoadArchive(name=archivename, status=LoadStatus.NEW.value, location=location)
            session.add(load_archive)
            session.flush()
            archive_id = load_archive.id

            with FTP() as ftp_client:
            
                ftp_client.connect(host, port)
                ftp_client.login(user, password)            
                ftp_client.cwd(location) 

                for filename, file_size, content in download_extract_zip(ftp_client, archivename):                
                    log.debug((filename, file_size, content))
                    load_file = LoadFile(archive_id=archive_id, name=filename, status=LoadStatus.COMPLETE.value)
                    session.add(load_file)

            load_archive.status = LoadStatus.COMPLETE.value

        archive_q.task_done()


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
                
                with thezip.open(zipinfo) as thefile:
                    yield zipinfo.filename, zipinfo.file_size, thefile.read()