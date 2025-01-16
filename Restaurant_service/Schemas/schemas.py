from pydantic import BaseModel
from typing import List
from datetime import datetime

class ItemBase(BaseModel):
    item_name: str
    item_description: str
    item_price: float
    restaurant_id: int

    class Config:
        orm_mode = True

class Item(ItemBase):
    item_id: int
    class Config:
        orm_mode = True


class RestaurantBase(BaseModel):
    restaurant_name: str
    restaurant_address: str
    restaurant_phone_number: int
    restaurant_email: str
    password: str
    restaurant_status: datetime

    class Config:
        orm_mode = True


class Restaurant(RestaurantBase):
    restaurant_id: int
    items: List[Item]

    class Config:
        orm_mode = True
