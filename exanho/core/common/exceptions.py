class ExanhoError(Exception):
    pass

class Error(ExanhoError):
    def __init__(self, message, inner=None, params=None):
        self.error = True
        self.message = message
        self.inner = inner
        self.params = params

