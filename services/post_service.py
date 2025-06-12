from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.post import Post, PostCreate
from app.models.user import User
from typing import List

# In-memory post cache
from cachetools import TTLCache

cache = TTLCache(maxsize=1000, ttl=300)  # 5 minutes TTL

def add_post(post_data: PostCreate, user: User, db: Session):
    if len(post_data.text.encode('utf-8')) > 1024 * 1024:
        raise HTTPException(status_code=413, detail="Post exceeds 1MB")

    post = Post(user_id=user.id, text=post_data.text)
    db.add(post)
    db.commit()
    db.refresh(post)

    cache.pop(user.id, None)  # invalidate cache
    return post.id

def get_posts(user: User, db: Session):
    if user.id in cache:
        return cache[user.id]

    posts = db.query(Post).filter(Post.user_id == user.id).all()
    cache[user.id] = posts
    return posts

def delete_post(post_id: int, user: User, db: Session):
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user.id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(post)
    db.commit()

    cache.pop(user.id, None)
    return {"message": "Post deleted"}
