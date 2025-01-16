from pydantic import BaseModel
from typing import List
from datetime import datetime

class itemBase(BaseModel):
    item_name: str
    item_description: str
    item_price: float
    restaurant_id: int

    class Config:
        orm_mode = True

class item(itemBase):
    item_id: int
    class Config:
        orm_mode = True


class restaurantBase(BaseModel):
    restaurant_name: str
    restaurant_address: str
    restaurant_phone_number: int
    restaurant_email: str
    password: str
    restaurant_status: datetime

    class Config:
        orm_mode = True

