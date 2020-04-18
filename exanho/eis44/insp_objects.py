import datetime
import os.path

class InspFile:

    def __init__(self, name:str, date:datetime.datetime, size = None):
        self._name = name
        self._fullpath = None
        self._date = date
        self._size = size

    @property
    def name(self):
        return self._name

    def set_fullpath(self, fullpath):
        self._fullpath = fullpath

    @property
    def fullpath(self):
        return self._fullpath

    @property
    def date(self):
        return self._date

    @property
    def size(self):
        return self._size

    def __str__(self):
        return 'InspFile: name={0.name}, fullpath={0.fullpath}, date={0.date}, size={0.size}'.format(self)

class InspDirectory:

    def __init__(self, path, only_inspect = False):
        self._path = path
        self._only_inspect = only_inspect

    def set_fullpath(self, fullpath):
        self._path = os.path.join(fullpath, self._path)

    @property
    def path(self):
        return self._path

    @property
    def only_inspect(self):
        return self._only_inspect