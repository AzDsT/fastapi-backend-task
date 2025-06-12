from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from pydantic import BaseModel, constr
from typing import List

# --- SQLAlchemy Post Model ---
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(String(1048576), nullable=False)  # ~1MB limit

    user = relationship("User")

# --- Pydantic Schemas ---

class PostCreate(BaseModel):
    text: constr(max_length=1048576)

class PostOut(BaseModel):
    id: int
    text: str
    class Config:
        orm_mode = True
