from pydantic import BaseModel
from typing import List, Optional


class item(BaseModel):
    item_id: int

    class Config:
        orm_mode = True


class item_with_quantity(BaseModel):
    item_id: int
    quantity: int

    class Config:
        orm_mode = True

class orderBase(BaseModel):
    user_id: int
    restaurant_id: int
    order_status: str
    total_bill: float
    delivery_driver: Optional[int] = 0

class createOrder(orderBase):
    items: List[item_with_quantity]
    class Config:
        orm_mode = True


class orderd_items(BaseModel):
    item_ids: List[int]
    restaurant_id: int

class items_with_price(BaseModel):
    item_id: int
    item_price: float


