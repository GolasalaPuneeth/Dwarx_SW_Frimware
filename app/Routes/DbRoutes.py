from fastapi import APIRouter, HTTPException, status, Request, Header, Depends
from DatabaseLayer import get_session
from ServiceLayer import IDbProcessor,DbProcessor

db_router = APIRouter(prefix="/UserCred", tags=["Database APIs"])
db_router_1 = APIRouter(prefix="/User", tags=["Database APIs"])
service : IDbProcessor = DbProcessor()

@db_router.post("/")
async def create_user(user_identity: str, passcode: str, session = Depends(get_session)):
    result: bool = await service.create_credentials(user_identity,passcode,session)
    if not result:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
    return result

@db_router.put("/")
async def update_pass(user_identity: str, new_passcode: str, session = Depends(get_session)):
    await service.update_credentials(user_identity,new_passcode,session)
    return True

@db_router.delete("/")
async def delete_user(user_identity: str,session = Depends(get_session)):
    await service.del_credentials(user_identity,session)
    return True

@db_router.get("/signup")
async def signup(user_identity: str, passcode: str, session = Depends(get_session)):
    return await service.check_credentials(user_identity,passcode,session)



