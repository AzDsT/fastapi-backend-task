# 🧠 FastAPI Backend Test Task – AI Financial Planning App

This project was developed as part of a backend developer test task for an AI-powered financial planning platform.

## ✅ Features Implemented

- Python 3.10 + FastAPI
- MVC architecture with clear separation of:
  - Routes
  - Services (business logic)
  - Models (SQLAlchemy + Pydantic)
  - Database config
  - Utility functions (auth, caching)
- MySQL-ready with SQLAlchemy ORM
- JWT-based token authentication
- Password hashing with bcrypt
- Dependency injection via FastAPI
- 1MB payload validation for AddPost
- In-memory response caching for GetPosts (5 min)
- Full validation for all fields via Pydantic
- Thoroughly documented code with comments

## 🚀 API Endpoints

### `/auth/signup`  
- Accepts: `email`, `password`
- Returns: access token

### `/auth/login`  
- Accepts: `email`, `password`
- Returns: access token

### `/post/add-post`  
- Auth token required
- Accepts: `text` (≤1MB)
- Returns: `post_id`

### `/post/posts`  
- Auth token required
- Returns: list of posts (cached 5 min)

### `/post/delete-post/{post_id}`  
- Auth token required
- Deletes user’s post



