import datetime
import re

from ftplib import FTP

import exanho.core.common.dt_utilities as dt_util
from exanho.ftp_loading.insp_objects import InspFile, InspDirectory

class FtpConsider:
    def __init__(self, *args, **kwargs):
        self.task_id = kwargs['task_id']
        self.insp_q = kwargs['insp_q']

        self.host = kwargs['host']
        self.port = kwargs['port']
        self.user = kwargs['user']
        self.password = kwargs['password']  

        self.location = kwargs['location']

        self.min_date = kwargs.get('min_date', dt_util.check_none_return_min())
        self.max_date = kwargs.get('max_date', dt_util.check_none_return_max())
        self.excluded_folders = kwargs.get('excluded_folders')
        self.delimiter = kwargs.get('delimiter', ',')

        self._one_pass_directories = []
        self._one_pass_files = []
        self._directories = []
        self.has_star = False

        self.now = datetime.datetime.now()

    def prepare(self):
        if not isinstance(self.min_date, datetime.datetime):
            self.min_date = datetime.datetime(datetime.MINYEAR, 1, 1)

        if not isinstance(self.max_date, datetime.datetime):
            self.max_date = datetime.datetime(datetime.MAXYEAR, 12, 31)

        if self.excluded_folders:
            self.excluded_folders = self.excluded_folders.split(self.delimiter)
            self.excluded_folders = [fld.strip() for fld in self.excluded_folders]
        else:
            self.excluded_folders = []

        parts = self.location.split('*')
        only_inspect = False
        if len(parts) > 1:
            self.has_star = True
            self._folder = parts[1].lstrip('\/')
            only_inspect = bool(self._folder)

        self._directories.append(InspDirectory(parts[0].rstrip('\/'), only_inspect))


    def _parse_retrline(self, line):
        permission, num, user, group, size, *date, ftp_object_name  = re.split(r'\s+', line)

        if permission.startswith('d'):
            if self.has_star and ftp_object_name not in self.excluded_folders:
                only_inspect = not ( not bool(self._folder) or (ftp_object_name == self._folder) )
                self._one_pass_directories.append(InspDirectory(ftp_object_name, only_inspect))
        else:
            create_dt = datetime.datetime(datetime.MINYEAR, 1, 1)
            if len(date) == 3:
                if date[2].isdigit(): # ['Apr', '08', '2018']
                    create_dt = datetime.datetime.strptime(''.join(date), '%b%d%Y')
                elif ':' in date[2]: # ['Apr', '08', '00:03']
                    current_year = datetime.date.today().year
                    create_dt = datetime.datetime.strptime('{}{}'.format(current_year, ''.join(date)), '%Y%b%d%H:%M')
                    if create_dt > self.now:
                        create_dt = create_dt.replace(year=(current_year-1))
            if create_dt >= self.min_date and create_dt < self.max_date:
                self._one_pass_files.append(InspFile(ftp_object_name, create_dt, size))

    def inspect(self):
        
        with FTP() as ftp_client:        
            ftp_client.connect(self.host, self.port)
            ftp_client.login(self.user, self.password)

            while self._directories:

                curr_directory = self._directories.pop(0)

                if (ftp_client.pwd() != curr_directory.path):
                    ftp_client.cwd(curr_directory.path)

                ftp_client.retrlines('LIST', callback=self._parse_retrline)

                if self._one_pass_directories:
                    list(map(lambda dir: dir.set_fullpath(curr_directory.path), self._one_pass_directories))
                    self._directories.extend(self._one_pass_directories)
                    self._one_pass_directories = []

                if self._one_pass_files and not curr_directory.only_inspect:
                    list(map(lambda dir: dir.set_fullpath(curr_directory.path), self._one_pass_files))
                    for insp_file in self._one_pass_files:
                        self.insp_q.put((self.task_id, insp_file.name, insp_file.fullpath, insp_file.date, insp_file.size))

                self._one_pass_files = []
