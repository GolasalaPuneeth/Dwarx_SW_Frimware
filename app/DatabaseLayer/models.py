from sqlmodel import SQLModel, Field
from datetime import datetime
from AppUtils import gadgets
import shortuuid

class UserOptions(SQLModel, table=True):
    __tablename__ = "user_options"
    id: str = Field(default_factory=shortuuid.uuid, primary_key=True)
    user_identity: str
    amt: float
    Liters: float

class UserCred(SQLModel, table=True):
    __tablename__ = "user_cred"
    user_identity :str = Field(primary_key=True)
    passcode : str

class UserDetails(SQLModel, table=True):
    __tablename__ = "user_details"
    user_identity : str = Field(primary_key=True)
    user_name: str
    user_mobile_number: str
    user_mail: str
    Account_num : str
    user_bank_ifsc : str
    user_bank_name : str
    user_address: str
    user_shop_image_url: str
    
class UserTrans(SQLModel,table = True):
    __tablename__ = "user_trans"
    user_identity : str
    trans_id : str = Field(primary_key=True)
    amt: float
    vpa: str
    trans_datetime: datetime = Field(default_factory=gadgets.get_ist_time)
    settled: bool = False
