from datetime import datetime
from pydantic import BaseModel


class UserResponse(BaseModel):
    id : int
    firstname : str
    lastname : str
    email_id : str
    password : str
    created_ts : datetime
    status : bool
    
    class Config:
        orm_mode : True
    
class UserCreate(BaseModel):
    firstname : str
    lastname : str
    email_id : str
    password : str
    
class UserLogin(BaseModel):
    email_id: str
    password: str