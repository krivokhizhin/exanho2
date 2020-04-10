import datetime
import re

from ftplib import FTP
from collections import namedtuple

from exanho.eis44.ftp_objects import FtpFile, FtpDirectory

class FtpExtractor:
    def __init__(self, *args, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
        self.user = kwargs['user']
        self.password = kwargs['password']
        self.location = kwargs['location']
        self.archive_queue = kwargs['archive_queue']

        self.begin_date = kwargs.get('begin_date', datetime.date(datetime.MINYEAR, 1, 1))
        self.end_date = kwargs.get('end_date', datetime.date(datetime.MAXYEAR, 12, 31))

        if self.begin_date > self.end_date:
            raise AssertionError(f'begin_date={self.begin_date} > end_date={self.end_date}')

        self.ftp_objects = []
        self.zipname_re = None

    # def initialize(self):
    #     self.region = self._extract_region(self.dirname)
    #     log.debug(self.region)

    #     pattern = None
    #     if self.region:
    #         pattern = '(?P<doctype>[^_]+)_('+self.region+'_)?(?P<begin_date>\d{10})_(?P<end_date>\d{10})(_(?P<manual_date>\d{14}))?_(?P<num>\d{3})\.xml\.zip'
    #     else:
    #         pattern = '(?P<doctype>[^_]+)_((all_(?P<begin_date>\d{14}))|(inc_(?P<begin_date>\d{14})_(?P<end_date>\d{14})))_(?P<num>\d{3})\.xml\.zip'
    #     self.zipname_re = re.compile(pattern)

    # def _extract_region(self, dirname):
    #     is_fcs_regions = False
    #     for part in dirname.split('/'):
    #         if is_fcs_regions:
    #             return part
    #         if part == 'fcs_regions':
    #             is_fcs_regions = True
        
    #     return None

    # def _parse_zipname(self, zipname):
    #     res = self.zipname_re.match(zipname)
    #     if res is None:
    #         return None, None, None, None, None
        
    #     doctype = res.group('doctype')
        
    #     b_d = res.group('begin_date')
    #     begin_date = None if b_d is None else datetime.datetime.strptime(b_d, '%Y%m%d%H').date()
        
    #     e_d = res.group('end_date')
    #     end_date = None if e_d is None else datetime.datetime.strptime(e_d, '%Y%m%d%H').date()
        
    #     md_d = res.group('manual_date')
    #     manual_date = None if md_d is None else datetime.datetime.strptime(md_d, '%Y%m%d%H%M%S').date()
        
    #     num = int(res.group('num'))
        
    #     return doctype, begin_date, end_date, manual_date, num

    def _parse_retrline(self, line):
        permission, num, user, group, size, *date, filename  = re.split(r'\s+', line)

        if permission.startswith('d'):
            self.ftp_objects.append(FtpDirectory(filename, size))
        else:
            create_dt = datetime.datetime(datetime.MINYEAR, 1, 1, 0, 0, 0, 0)
            if len(date) == 3:
                if date[2].isdigit(): # ['Apr', '08', '2018']
                    create_dt = datetime.datetime.strptime(''.join(date), '%b%d%Y')
                elif ':' in date[2]: # ['Apr', '08', '00:03']
                    current_year = datetime.date.today().year
                    create_dt = datetime.datetime.strptime('{}{}'.format(current_year, ''.join(date)), '%Y%b%d%H:%M')
            self.ftp_objects.append(FtpFile(filename, create_dt, size))

        # create_dt = None
        # if len(date) == 3:
        #     current_year = datetime.date.today().year
        #     create_dt = datetime.datetime.strptime('{}{}'.format(current_year, ''.join(date)), '%Y%b%d%H:%M')

        # parts = re.split(r'\s+', line)
        # doctype, begin_date, end_date, manual_date, num = self._parse_zipname(parts[-1])

        # if not begin_date or not end_date or begin_date < self.begin_date or end_date > self.end_date:
        #     return

    def _try_select_archive(self, zipname):
        pass

    def extract(self):

        with FTP() as ftp_client:
        
            ftp_client.connect(self.host, self.port)
            ftp_client.login(self.user, self.password)
            
            ftp_client.cwd(self.location)            
            list_cmd = ftp_client.retrlines('LIST', callback=self._parse_retrline)

            archives = [ftp_object for ftp_object in self.ftp_objects if isinstance(ftp_object, FtpFile)]

            for archive in sorted(archives, key=lambda archive: archive.date):
                self.archive_queue.put((self.location, archive.name))

            # with open('output.txt', 'wt') as f:
            #     for archive_name in self.archive_names:
            #         f.write(archive_name+'\n')
            
        # for archive_name in self.archive_names:
        #     print(archive_name)