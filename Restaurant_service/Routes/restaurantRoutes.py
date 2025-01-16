from fastapi import  APIRouter,Depends,HTTPException, status
from fastapi.security import APIKeyHeader
from DatabaseConfig.databaseConfig import get_db
from Schemas import schemas
from sqlalchemy.orm import Session


authorization_scheme = APIKeyHeader(name="Authorization", auto_error=True)

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/register/restaurant')
def registerRestaurant(request: schemas.orderCreate, db:Session=Depends(get_db)):
    return "hello"