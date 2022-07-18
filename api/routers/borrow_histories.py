from fastapi import APIRouter
from models.borrow_histories import Borrow_histories
from peewee import fn

router = APIRouter()

@router.get("/api/numbers_borrow/", tags=["borrow_histories"])
async def read_borrow_histories():
    numbers_borrow = (Borrow_histories
                        .select(Borrow_histories.book_id, fn.COUNT(Borrow_histories.id).alias('total'))
                        .group_by(Borrow_histories.book_id)
                        .order_by(Borrow_histories.book_id))
    result = []
    for number_borrow in numbers_borrow:
        result.append({"book_id": number_borrow.book_id.id, "number_borrow": number_borrow.total})
    return result
