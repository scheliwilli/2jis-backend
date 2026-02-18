from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app import models, schemas
from app.dependencies import get_db, get_current_user, get_admin_user

router = APIRouter(prefix="/places", tags=["Places"])


@router.post("/", response_model=schemas.PlaceOut)
def create_place(place: schemas.PlaceCreate,
                 db: Session = Depends(get_db),
                 user=Depends(get_current_user)):

    new_place = models.Place(**place.dict())
    db.add(new_place)
    db.commit()
    db.refresh(new_place)
    return new_place


@router.get("/", response_model=list[schemas.PlaceOut])
def get_places(min_rating: Optional[float] = None,
               db: Session = Depends(get_db)):

    query = db.query(models.Place)

    if min_rating is not None:
        query = query.filter(models.Place.average_rating >= min_rating)

    return query.all()


@router.delete("/{place_id}")
def delete_place(place_id: int,
                 db: Session = Depends(get_db),
                 admin=Depends(get_admin_user)):

    place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not place:
        raise HTTPException(404, "Такого места нет(")

    db.delete(place)
    db.commit()
    return {"message": "Место удалено"}
