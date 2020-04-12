import datetime
import re

from ftplib import FTP
from collections import namedtuple

from exanho.eis44.ftp_objects import FtpFile, FtpDirectory

class FtpConsider:
    def __init__(self, *args, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
        self.user = kwargs['user']
        self.password = kwargs['password']
        self.location = kwargs['location']

        self.ftp_objects = []
        self.zipname_re = None

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

    def _try_select_archive(self, zipname):
        pass

    def consider(self):

        with FTP() as ftp_client:
        
            ftp_client.connect(self.host, self.port)
            ftp_client.login(self.user, self.password)
            
            ftp_client.cwd(self.location)            
            list_cmd = ftp_client.retrlines('LIST', callback=self._parse_retrline)