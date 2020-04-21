from abc import ABC, abstractmethod

class IParse(ABC):

    @abstractmethod
    def parse(self, filename, size, message, update=False):
        pass