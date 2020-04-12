import datetime

class FtpFile:

    def __init__(self, name:str, date:datetime.datetime, size = None):
        self._name = name
        self._date = date
        self._size = size

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    @property
    def size(self):
        return self._size

    def __str__(self):
        return 'FtpFile: name={0.name}, date={0.date}, size={0.size}'.format(self)

class FtpDirectory:

    def __init__(self, directory, size = None):
        self._directory = directory
        self._size = size

    @property
    def directory(self):
        return self._directory

    @property
    def size(self):
        return self._size