from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import UserCreate, UserLogin
from services import user_service
from db.database import get_db


router = APIRouter()

@router.post("/signup")
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user and return an access token.
    """
    token = user_service.create_user(user_data, db)
    return {"access_token": token}

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate user and return an access token.
    """
    token = user_service.login_user(user_data, db)
    return {"access_token": token}
