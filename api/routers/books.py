from fastapi import APIRouter
from models.books import Books

router = APIRouter()


@router.get("/books/", tags=["books"])
async def read_books():
    books = Books.select()
    result = []
    for book in books:
        result.append({"id": book.id, "name": book.name, "category_name": book.category_id.name, "user_name": book.user_id.name, "status": book.book_status})
    return (result)


@router.get("/cart/{user_id}", tags=["cart"])
async def read_cart(user_id):
    books = Books.select().where(Books.user_id == user_id)
    result = []
    for book in books:
        result.append({"id": book.id, "name": book.name})
    return (result)
