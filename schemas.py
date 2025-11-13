from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# 🔹 Схемы для мест
class PlaceBase(BaseModel):
    name: str
    description: Optional[str] = None
    address: Optional[str] = None
    latitude: float
    longitude: float
    category: Optional[str] = None
    wheelchair_accessible: bool = False
    has_ramp: bool = False
    has_elevator: bool = False
    door_width: Optional[int] = None

class PlaceCreate(PlaceBase):
    pass

class PlaceResponse(PlaceBase):
    id: int
    created_at: datetime
    is_verified: bool
    
    class Config:
        orm_mode = True

# 🔹 Схемы для отзывов
class ReviewBase(BaseModel):
    text: str
    rating: int  # 1-5

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: int
    user_id: int
    place_id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

# 🔹 Схема для места с отзывами
class PlaceWithReviewsResponse(BaseModel):
    place: PlaceResponse
    reviews: List[ReviewResponse]
    reviews_count: int
    average_rating: float