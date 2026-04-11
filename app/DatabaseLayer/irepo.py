from abc import ABC,abstractmethod
from dataclasses import dataclass
from .db import AsyncSession
from .models import UserCred

class Irepository(ABC):

    @abstractmethod
    async def create_user_id_pass(self,user_info : UserCred, session: AsyncSession) -> bool:
        """
        This API is used to create User_id and Password        
        """
        raise NotImplementedError

    @abstractmethod
    async def check_user_exist(self, user_identity: str, session: AsyncSession) -> str | None:
        """
        This API is used to get password for user_identity
        """
        raise NotImplementedError
    
    @abstractmethod
    async def update_user_pass(self, user_identity: str, new_pass: str, session: AsyncSession) -> bool|None:
        """
        This API is used to update user password
        
        """
        raise NotImplementedError
    
    @abstractmethod
    async def delete_user_cred(self, user_identity: str, session: AsyncSession) -> bool|None:
        """
        This API is used to Delete User

        """
        raise NotImplementedError