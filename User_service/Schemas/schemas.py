from typing import List, Optional
from pydantic import BaseModel



class Role(BaseModel):
    role_id: Optional[int]
    role_type: str

    class Config:
        orm_mode = True



class User(BaseModel):
    user_id: Optional[int]
    full_name: str
    user_name: str
    email: str
    password: str
    phoneNumber: int
    address: str
    roleStatus: str
    activeRole: str
    roles: Optional[List[Role]]

    class Config:
        orm_mode = True


class Credentials(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class auth_payload(BaseModel):
    id:int
    role:str


class refresh_token(BaseModel):
    refresh_token:str


class order_details(BaseModel):
    order_id: int
    order_status: str

class order_payload(order_details):
    id: int
