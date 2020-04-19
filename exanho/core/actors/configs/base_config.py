import logging

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
            elif isinstance(value,list):
                dic.setdefault(key, [])
                for item in value:
                    if isinstance(item, ConfigBase):
                        dic[key].append(item.serialize())
                    else:
                        dic[key].append(item)
            else:
                dic[key] = value
        return dic

    @classmethod
    def create_instance(cls, dic: dict):
        return cls(dic)


class ConfigBaseDerived:

    def __init__(self, config_class):
        if not issubclass(config_class, ConfigBase):
            raise TypeError(f'Expected derived from the ConfigBase class, and the class specified {str(config_class)}.')

        self.config_class = config_class

    def __set_name__(self, owner, name):
        self.name = name   

    def __get__(self, obj, type=None):
        if self.name not in obj.__dict__:
            return None
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        obj.__dict__[self.name] = self.config_class.create_instance(value)


class ListConfigBaseDerived(ConfigBaseDerived):

    def __set__(self, obj, value):
        if not isinstance(value, list):
            raise TypeError('Expected a list, but {} is received.'.format(type(value)))

        item_list = []
        for item in value:
            item_list.append(self.config_class.create_instance(item))
        obj.__dict__[self.name] = item_list

class List(ConfigBase):
    pass