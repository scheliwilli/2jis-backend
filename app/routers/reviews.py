from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas
from app.dependencies import get_db, get_current_user

router = APIRouter(prefix="/reviews", tags=["Reviews"])


@router.get("/{place_id}")
def list_reviews(place_id: int, db: Session = Depends(get_db)):
    place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not place:
        raise HTTPException(404, "Такого места пока нет")

    reviews = (
        db.query(models.Review)
        .filter(models.Review.place_id == place_id)
        .order_by(models.Review.created_at.desc())
        .all()
    )

    return [
        {
            "id": r.id,
            "user_id": r.user_id,
            "rating": r.rating,
            "comment": r.comment,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in reviews
    ]


@router.get("/{place_id}/me")
def my_review(place_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not place:
        raise HTTPException(404, "Такого места пока нет")

    r = (
        db.query(models.Review)
        .filter(models.Review.place_id == place_id, models.Review.user_id == user.id)
        .first()
    )
    if not r:
        raise HTTPException(404, "No review")

    return {
        "id": r.id,
        "user_id": r.user_id,
        "rating": r.rating,
        "comment": r.comment,
        "created_at": r.created_at.isoformat() if r.created_at else None,
    }


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
        raise HTTPException(400, "Нужно оценить это место")

    new_review = models.Review(
        rating=review.rating,
        comment=review.comment,
        user_id=user.id,
        place_id=place_id
    )

    db.add(new_review)
    db.commit()


    avg = db.query(func.avg(models.Review.rating)).filter(
        models.Review.place_id == place_id
    ).scalar()

    place.average_rating = round(avg, 2)
    db.commit()

    return {"message": "Ваш отзыв добавлен", "рейтинг": place.average_rating}
