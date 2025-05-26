from typing import Union
from pydantic import BaseModel




class UserBase(BaseModel):
    login:str

class UserDB(UserBase):
    password:str


class UserCreate(UserBase):
    password:str


class User(UserBase):
    id: int
    class Config:
        from_attributes = True