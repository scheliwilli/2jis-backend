from fastapi import FastAPI, HTTPException, Depends
from fastapi.middle.cors import CORSMiddleware
from database import engine, Base
import models

app = FastAPI()

@app get("/points")
async def root():
    return {"points":""}

Base.metadata.create_all(bing=engine)