from sqlalchemy.orm import Session
from Model import model
from fastapi import HTTPException, status

def create_default_roles(db: Session):
    # Define default roles
    default_roles = ["admin", "customer", "deliverydriver"]

    # Check if each role already exists
    existing_roles = db.query(model.Role.role_type).filter(model.Role.role_type.in_(default_roles)).all()
    existing_role_types = [role[0] for role in existing_roles]

    # Insert roles that don't already exist
    for role in default_roles:
        if role not in existing_role_types:
            new_role = model.Role(role_type=role)
            db.add(new_role)

    # Commit changes to the database
    db.commit()
    return {"message": "Default roles created successfully"}
