from pydantic import BaseModel
from typing import List
from datetime import datetime

class itemBase(BaseModel):
    item_name: str
    item_description: str
    item_price: float

    class Config:
        orm_mode = True

class item(itemBase):
    item_id: int
    class Config:
        orm_mode = True


class restaurantBase(BaseModel):
    restaurant_name: str
    restaurant_address: str
    restaurant_phone_number: str
    restaurant_email: str
    password: str
    restaurant_status: str

    class Config:
        orm_mode = True

class restaurant(restaurantBase):
    restaurant_id: int
    class Config:
        orm_mode = True


class orderd_items(BaseModel):
    item_ids: List[int]
    restaurant_id: int

class items_with_price(BaseModel):
    item_id: int
    item_price: float


class credentials(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class payload(BaseModel):
    id:int
    role:str

class refresh_token(BaseModel):
    refresh_token:str

