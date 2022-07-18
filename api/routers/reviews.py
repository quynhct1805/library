from fastapi import APIRouter
from models.reviews import Reviews

router = APIRouter()

@router.get("/api/reviews_book/{book_id}", tags=["reviews"])
async def read_reviews_book(book_id):
    reviews = Reviews.select().where(Reviews.book_id == book_id)
    result = []
    for review in reviews:
        result.append({"user": review.user_id.name, "rate": review.rate_stars, "cmt": review.comment, "created_at": review.created_at})
    return (result)