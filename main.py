from fastapi import FastAPI

app = FastAPI(
    title="Карта доступности API",
    description="API для карты доступности городов",
    version="1.0.0"
)

@app get("/")
async def root():
    return ["message": "Добро пожаловать на карту доступности города"]
