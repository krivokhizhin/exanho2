class ConfigBase():

    def __init__(self, dic: dict):
        if not isinstance(dic, dict):
            raise TypeError('Expected a dict, but {} is received.'.format(type(dic)))

        for key, value in dic.items():
            setattr(self, key, value)

    def serialize(self):
        dic = {}
        for key, value in self.__dict__.items():
            if isinstance(value, ConfigBase):
                dic[key] = value.serialize()
            else:
                dic[key] = value
        return dic

    @classmethod
    def create_instance(cls, dic: dict):
        return cls(dic)


class ReadOnlyConfigBaseDerived:
    expected_type = None

    def __init__(self, config_class):
        if not issubclass(config_class, ConfigBase):
            raise TypeError(f'Expected derived from the ConfigBase class, and the class specified {str(config_class)}.')

        self.config_class = config_class
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

        obj.__dict__[self.name] = self.config_class.create_instance(value)
        self.init = True