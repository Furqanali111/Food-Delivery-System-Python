from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Model import model
from Schemas import schemas


def createUser(request: schemas.orderCreate, db: Session):
    [db.add(item) for item in request.items]

    new_order= model.Order(
        user_id=request.user_id,
        restaurant_id=request.restaurant_id,
        delivery_driver=request.delivery_driver,
        order_status=request.order_status,
        total_bill=request.total_bill,
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


def fetchOrder(order_id: int, db: Session):
    user = db.query(model.Order).filter(model.Order.order_id == order_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with the id {order_id} is not available")

    db.commit()

    return user
