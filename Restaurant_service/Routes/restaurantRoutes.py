from fastapi import  APIRouter,Depends,HTTPException, status
from fastapi.security import APIKeyHeader
from DatabaseConfig.databaseConfig import get_db
from Schemas import schemas
from sqlalchemy.orm import Session
from Repository import restaurantRepo


authorization_scheme = APIKeyHeader(name="Authorization", auto_error=True)

router = APIRouter(
    prefix="/restaurant",
    tags=['Restaurant']
)

@router.post('/register/restaurant')
def registerRestaurant(request: schemas.restaurantBase, db:Session=Depends(get_db)):
    return restaurantRepo.createRestaurant(request,db)
