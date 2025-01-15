from fastapi import  APIRouter,Depends,HTTPException, status
from fastapi.security import APIKeyHeader
from DatabaseConfig.databaseConfig import get_db
from Schemas import schemas
from Repository import userRepo
from sqlalchemy.orm import Session
from Client import authClient
from Utils import utils
from MiddleWare import middleware

authorization_scheme = APIKeyHeader(name="Authorization", auto_error=True)

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/register/user')
def createUser(request: schemas.User, db:Session=Depends(get_db)):
    return userRepo.createUser(request, db)


@router.post('/login')
def login(request: schemas.Credentials, db:Session=Depends(get_db)):
    user = userRepo.login(request, db)
    payload = utils.create_payload_obj(user.user_id, user.activeRole)

    try:
        response = authClient.create_token(payload)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"error in authentication service : {e}"
        )

    return

@router.post('/refresh/token')
def refresh_token(request: schemas.refresh_token):

    try:
        response = authClient.refresh_token(request)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"error in authentication service : {e}"
        )

    return

@router.delete('/delete/user')
def deleteUser(request: schemas.Credentials, db:Session=Depends(get_db), token_payload: dict = Depends(middleware.validate_token)):
    return userRepo.deleteUser(request, db)


@router.get(f'/fetch/user',response_model=schemas.User)
def fetchUser(db:Session=Depends(get_db), token_payload: dict = Depends(middleware.validate_token)):
    return userRepo.fetchUser(token_payload['id'], db)


