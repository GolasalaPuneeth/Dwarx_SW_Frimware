from abc import ABC,abstractmethod
from DatabaseLayer  import AsyncSession


class IDbProcessor(ABC):

    @abstractmethod
    async def create_credentials(self, user_identity:str, passcode:str, session: AsyncSession) -> bool:
        """
        Service layer to create credentials
        
        """
        raise NotImplementedError
    
    @abstractmethod
    async def check_credentials(self, user_identity:str, passcode:str, session: AsyncSession) -> bool:
        """
        Service layer to check credentials
        
        """
        raise NotImplementedError
    
    @abstractmethod
    async def update_credentials(self,user_identity:str, new_passcode:str, session: AsyncSession) -> bool:
        """
        Service layer to update credentials
        
        """
        raise NotImplementedError
    
    @abstractmethod
    async def del_credentials(self,user_identity:str, session: AsyncSession)-> bool :
        """
        Service Layer to delete User
        
        """
        raise NotImplementedError