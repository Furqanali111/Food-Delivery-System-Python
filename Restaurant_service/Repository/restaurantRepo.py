from logging import raiseExceptions
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Model import model
from Schemas import schemas
from Hashing.hash import Hash


def createRestaurant(request: schemas.restaurantBase, db: Session):
    new_restaurant = model.Restaurant(
        restaurant_name=request.restaurant_name,
        restaurant_address=request.restaurant_address,
        restaurant_phone_number=request.restaurant_phone_number,
        restaurant_email=request.restaurant_email,
        password=Hash.bcrypt(request.password),
        restaurant_status=request.restaurant_status
    )

    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant

