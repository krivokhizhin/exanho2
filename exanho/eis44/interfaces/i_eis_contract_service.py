from abc import ABC, abstractmethod

from . import ContractInfo

class IEisContractService(ABC):
    
    @abstractmethod
    def get_contract(self, reg_num:str) -> ContractInfo:
        pass