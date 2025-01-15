
from sqlalchemy.orm import Session
from Model import model
from Schemas import schemas
from Hashing.hash import Hash
from fastapi import HTTPException, status


def create(request: schemas.User, db: Session):

    roles = db.query(model.Role).filter(model.Role.role_id.in_(request.roles)).all()

    new_user = model.User(
        full_name=request.full_name,
        email=request.email,
        password=Hash.bcrypt(request.password),
        user_name=request.user_name,
        phoneNumber=request.phoneNumber,
        address=request.address,
        roleStatus=request.roleStatus,
        activeRole=request.activeRole,
        roles=roles  # Pass Role objects, not just IDs
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user
