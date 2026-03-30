from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    age: int
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class PlaceCreate(BaseModel):
    name: str
    description: Optional[str]
    latitude: float
    longitude: float


class PlaceOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    latitude: float
    longitude: float
    average_rating: float

    class Config:
        from_attributes = True


class ReviewCreate(BaseModel):
    rating: int
    comment: Optional[str]


class SupportMessage(BaseModel):
    email: EmailStr
    subject: str
    message: str
