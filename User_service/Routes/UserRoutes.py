from fastapi import  APIRouter,Depends
from DatabaseConfig.databaseConfig import get_db
from Schemas import schemas
from Repository import userRepo
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/fetch/user')
def fetch_user(request: schemas.User, db:Session=Depends(get_db)):
    try:
        userRepo.create(request, db)
        return "User have been created successfully"
    except Exception as e:
        return  f"error while creating user error: {e}"