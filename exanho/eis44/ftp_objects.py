class FtpFile:

    def __init__(self, name, size = None):
        self._name = name
        self._size = size

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

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