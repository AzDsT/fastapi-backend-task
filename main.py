from fastapi import FastAPI
from app.routes import user_routes, post_routes
from app.db.database import Base, engine
from app.routes import user_routes, post_routes


# Create all DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Financial Platform Backend")

# Include routes
app.include_router(user_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(post_routes.router, prefix="/post", tags=["Posts"])
