from sqlalchemy.orm import Session
from models.user import User, UserCreate
from utils.auth import get_password_hash, verify_password, create_access_token
from fastapi import HTTPException, status
from models.user import User


def create_user(user_data: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = get_password_hash(user_data.password)
    user = User(email=user_data.email, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return create_access_token({"sub": user.email})

def login_user(user_data: UserCreate, db: Session):
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return create_access_token({"sub": user.email})
