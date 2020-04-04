from abc import ABC, abstractmethod

class INsiOrgTypeService(ABC):

    @abstractmethod
    def put(self, code, name, desc=None):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def get_by_code(self, code):
        pass