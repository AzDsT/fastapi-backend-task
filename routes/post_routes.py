from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.post import PostCreate, PostOut
from app.services import post_service
from app.utils.dependencies import get_current_user
from app.db.database import get_db
from typing import List

router = APIRouter()

@router.post("/add-post")
def add_post(
    post_data: PostCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    """
    Add a new post (limit 1MB), returns post ID.
    """
    post_id = post_service.add_post(post_data, user, db)
    return {"post_id": post_id}

@router.get("/posts", response_model=List[PostOut])
def get_posts(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    """
    Get all posts for the authenticated user (cached for 5 minutes).
    """
    return post_service.get_posts(user, db)

@router.delete("/delete-post/{post_id}")
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    """
    Delete a specific post by post ID.
    """
    return post_service.delete_post(post_id, user, db)
