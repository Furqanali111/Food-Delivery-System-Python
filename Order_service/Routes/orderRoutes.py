from fastapi import  APIRouter,Depends,HTTPException, status
from fastapi.security import APIKeyHeader
from DatabaseConfig.databaseConfig import get_db
from Repository import orderRepo
from Schemas import schemas
from sqlalchemy.orm import Session
from Utils import utils
from Client import restaurantClient

authorization_scheme = APIKeyHeader(name="Authorization", auto_error=True)

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/create/order',response_model=schemas.orderBase)
def createOrder(request: schemas.createOrder, db:Session=Depends(get_db)):
    ordered_items=utils.create_ordered_items_obj(request)
    response=restaurantClient.fetch_item_prices(ordered_items)
    print("response; ",response)
    total_bill = 0.0

    for item in request.items:
        item_price = next((item_price['item_price'] for item_price in response if item_price['item_id'] == item.item_id), 0)
        total_bill += item_price * item.quantity

    request.total_bill=total_bill
    return orderRepo.createOrder(request, db)