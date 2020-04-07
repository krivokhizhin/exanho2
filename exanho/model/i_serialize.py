class ISerializeToDict():

    def serialize(self):
        return {'class': self.__class__.__name__}