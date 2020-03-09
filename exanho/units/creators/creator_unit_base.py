from abc import ABC, abstractmethod

class UnitCreatorBase(ABC):

    @abstractmethod
    def get_unit_class(self):
        """
        factory_method
        """
        pass

    def instance(self, *args, **kwargs):
        return self.get_unit_class()(*args, **kwargs)

    # def terminate(self):
    #     return self.get_unit_class().terminate

    # def validate(self, *args, **kwargs):
    #     return self.get_unit_class().validate

