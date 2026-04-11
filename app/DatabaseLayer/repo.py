from .irepo import Irepository
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select
from fastapi import HTTPException,status
from DatabaseLayer.models import UserCred

class repository(Irepository):
    async def create_user_id_pass(self, user_info, session):
        try:
            session.add(user_info)
            await session.commit()
            # await session.refresh(user_info)
            return True

        except SQLAlchemyError as e:
            await session.rollback()  
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail=f"{e}")
        
    async def check_user_exist(self, user_identity, session):
        result = await session.execute(
            select(UserCred.passcode).where(UserCred.user_identity == user_identity)
        )
        # print(result.scalar_one_or_none(),"<-----")
        return result.scalar_one_or_none()
    
    async def update_user_pass(self, user_identity, new_pass, session):
        try:
            result = await session.execute(
                select(UserCred).where(UserCred.user_identity == user_identity)
                )
            user_info = result.scalar_one_or_none()
            if not user_info:
                return None
            user_info.passcode = new_pass
            await session.commit()
            # await session.refresh(user_info)
            return True
        except SQLAlchemyError as e:
            session.rollback()
            raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR ,detail=f"{e}")
        
    async def delete_user_cred(self, user_identity, session):
        try:
            result = await session.execute(
                select(UserCred).where(UserCred.user_identity == user_identity)
                )
            user_info = result.scalar_one_or_none()
            if not user_info:
                return None
            await session.delete(user_info)
            await session.commit()
            # await session.refresh(user_info)
            return True
        except SQLAlchemyError as e:
            session.rollback()
            raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR ,detail=f"{e}")
        
            