from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import users, places, reviews, support
from app.routers import navigat

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Карта доступности города")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(places.router)
app.include_router(reviews.router)
app.include_router(support.router)
app.include_router(navigat.router, prefix="/api")
