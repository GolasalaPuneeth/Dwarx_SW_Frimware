from abc import ABC,abstractmethod


class IcustomerRequest(ABC):

    @abstractmethod
    async def forward_to_esp(self,qrid:str,amount:str,vpa:str) -> bool:
        pass