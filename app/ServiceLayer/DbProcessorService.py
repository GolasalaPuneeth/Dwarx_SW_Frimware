from .IDbProcessorService import IDbProcessor
from DatabaseLayer import Irepository, repository
from DatabaseLayer.models import UserCred
from fastapi import HTTPException, status


class DbProcessor(IDbProcessor):
    def __init__(self):
        self.repo : Irepository = repository()

    async def create_credentials(self, user_identity, passcode, session):
        user_info : UserCred = UserCred(
            user_identity=user_identity,
            passcode=passcode
        )
        await self.repo.create_user_id_pass(user_info,session)
        return True
    
    async def check_credentials(self, user_identity, passcode, session):
        res: str = await self.repo.check_user_exist(user_identity,session)      
        if not res:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "User Not Found") 
        if res == passcode :
            return True
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Invalid Password")
        
    async def update_credentials(self, user_identity, new_passcode, session):
        res = await self.repo.update_user_pass(user_identity,new_passcode,session)
        if not res:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")        
        return True
    
    async def del_credentials(self, user_identity, session):
        res = await self.repo.delete_user_cred(user_identity, session)
        if not res:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
        return True