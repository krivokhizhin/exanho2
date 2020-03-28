class ReadOnlyTyped:
    expected_type = type(None)

    def __init__(self):
        self.init = False 

    def __set_name__(self, owner, name):
        self.name = name       

    def __get__(self, obj, type=None):
        if not self.init:
            raise AttributeError(f'The "{self.name}" item has not yet been initialized.')

        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if self.init:
            raise AttributeError(f'The "{self.name}" item is read-only.')

        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))

        obj.__dict__[self.name] = value
        self.init = True
        

class String(ReadOnlyTyped):
    expected_type = str

class Integer(ReadOnlyTyped):
    expected_type = int