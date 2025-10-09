from fastapi import FastAPI, HTTPException, Depends
from fastapi.middle.cors import CORSMiddleware
from database import engine, Base
import models

app = FastAPI(
    title="Карта доступности API",
    description="API для карты доступности городов",
    version="1.0.0"
)

@app get("/points")
async def root():
    return {"points":""}

Base.metadata.create_all(bing=engine)