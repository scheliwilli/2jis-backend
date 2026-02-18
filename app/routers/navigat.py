from fastapi import APIRouter
from pydantic import BaseModel
from app.services.navigation import calculate_accessible_route

router = APIRouter()

class RouteRequest(BaseModel):
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    user_type: str = "wheelchair"

@router.post("/route")
def get_route(request: RouteRequest):
    route = calculate_accessible_route(
        request.start_lat,
        request.start_lon,
        request.end_lat,
        request.end_lon,
        request.user_type
    )
    return {"route": route}