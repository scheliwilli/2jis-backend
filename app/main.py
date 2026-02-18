from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, places, reviews, support
from app.routers import navigation

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Карта доступности города")

app.include_router(users.router)
app.include_router(places.router)
app.include_router(reviews.router)
app.include_router(support.router)
app.include_router(navigation.router, prefix="/api")
