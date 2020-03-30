class Typed:
    expected_type = type(None)

    def __set_name__(self, owner, name):
        self.name = name    

    def __get__(self, obj, type=None):
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