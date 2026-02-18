from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas
from app.dependencies import get_db, get_current_user

router = APIRouter(prefix="/reviews", tags=["Reviews"])


@router.post("/{place_id}")
def add_review(place_id: int,
               review: schemas.ReviewCreate,
               db: Session = Depends(get_db),
               user=Depends(get_current_user)):

    place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not place:
        raise HTTPException(404, "Такого места пока нет")
 # запрет повтороной оценки???
    existing_review = db.query(models.Review).filter(
        models.Review.place_id == place_id,
        models.Review.user_id == user.id
    ).first()

    if existing_review:
        raise HTTPException(400, "You have already rated this place")

    new_review = models.Review(
        rating=review.rating,
        comment=review.comment,
        user_id=user.id,
        place_id=place_id
    )

    db.add(new_review)
    db.commit()

# ср рейтинг
    avg = db.query(func.avg(models.Review.rating)).filter(
        models.Review.place_id == place_id
    ).scalar()

    place.average_rating = round(avg, 2)
    db.commit()

    return {"message": "Ваш отзыв добавлен", "рейтинг": place.average_rating}
