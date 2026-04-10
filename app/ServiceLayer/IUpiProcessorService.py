from abc import ABC,abstractmethod

class IcustomerRequest(ABC):
    @abstractmethod
    async def push_service(self,qrid:str,amount:float,vpa:str) -> bool:
        raise NotImplementedError