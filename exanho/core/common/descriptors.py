class Typed:
    expected_type = type(None)

    def __init__(self, default=None):
        self.default = default

    def __set_name__(self, owner, name):
        self.name = name    

    def __get__(self, obj, type=None):
        if self.name not in obj.__dict__:
            return self.default
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))

        obj.__dict__[self.name] = value

class Boolean(Typed):
    expected_type = bool

class String(Typed):
    expected_type = str

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class List(Typed):
    expected_type = list