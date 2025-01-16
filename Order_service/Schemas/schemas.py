from pydantic import BaseModel
from typing import List, Optional


class item(BaseModel):
    item_id: int

    class Config:
        orm_mode = True

class orderBase(BaseModel):
    user_id: int
    restaurant_id: int
    order_status: str
    total_bill: float
    delivery_driver: Optional[int] = 0

class orderCreate(orderBase):
    items: List[item]

