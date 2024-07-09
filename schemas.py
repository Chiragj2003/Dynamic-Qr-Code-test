
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    full_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str
