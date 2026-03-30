from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine, SessionLocal
from app.routers import users, places, reviews, support
from app.routers import navigat
from app import models

Base.metadata.create_all(bind=engine)

def init_db():
    db = SessionLocal()
    try:
        if db.query(models.Place).count() == 0:
            mock_places = [
                models.Place(
                    name='ТЦ "Март"',
                    description='Торговый центр с хорошей доступностью',
                    latitude=55.0421,
                    longitude=82.9015,
                    average_rating=4.5,
                ),
                models.Place(
                    name='Театр драмы имени Лермонтова',
                    description='Исторический театр в центре города',
                    latitude=55.0367,
                    longitude=82.8985,
                    average_rating=4.2,
                ),
                models.Place(
                    name='Музей изобразительных искусств',
                    description='Музей с современными удобствами',
                    latitude=55.0445,
                    longitude=82.9078,
                    average_rating=4.8,
                ),
                models.Place(
                    name='Парк Гагарина',
                    description='Большой парк в центре города',
                    latitude=55.0295,
                    longitude=82.9125,
                    average_rating=3.9,
                ),
                models.Place(
                    name='Кинотеатр "Октябрь"',
                    description='Современный кинотеатр',
                    latitude=55.0528,
                    longitude=82.8923,
                    average_rating=4.6,
                ),
                models.Place(
                    name='Библиотека имени Муромцева',
                    description='Центральная библиотека с доступным входом',
                    latitude=55.0380,
                    longitude=82.9045,
                    average_rating=4.3,
                ),
                models.Place(
                    name='Государственный музей истории и культуры',
                    description='Музей с информацией об истории Новосибирска',
                    latitude=55.0405,
                    longitude=82.8945,
                    average_rating=4.4,
                ),
                models.Place(
                    name='Сквер Гвардейцев-панфиловцев',
                    description='Мемориал с ухоженной территорией',
                    latitude=55.0350,
                    longitude=82.9065,
                    average_rating=4.0,
                ),
            ]
            for place in mock_places:
                db.add(place)
            db.commit()
    finally:
        db.close()

init_db()

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
