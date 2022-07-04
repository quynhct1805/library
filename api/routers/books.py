from fastapi import APIRouter
from models.books import Books

router = APIRouter()


@router.get("/api/books/", tags=["books"])
async def read_books():
    books = Books.select()
    result = []
    for book in books:
        result.append({"id": book.id, "name": book.name, "category_id": book.category_id.id, "status": book.book_status, "image": book.images})
    return (result)


@router.get("/cart/{user_id}", tags=["cart"])
async def read_cart(user_id):
    books = Books.select().where(Books.user_id == user_id)
    result = []
    for book in books:
        result.append({"id": book.id, "name": book.name})
    return (result)
    

@router.post("/api/books/", tags=["books"])
async def create_book():
    book = Books.create(name="Vợ nhặt", category_id=1, images="")


@router.get("/api/book/{book_id}", tags=["books"])
async def read_book(book_id):
    books = Books.select().where(Books.id == book_id)
    for book in books:
        return({"id": book.id, "name": book.name, "category_id": book.category_id.id, "status": book.book_status, "image" : book.images})


@router.get("/api/books/{category_id}", tags=["books"])
async def read_books(category_id):
    books = Books.select().where(Books.category_id == category_id)
    result = []
    for book in books:
        result.append({"id": book.id, "name": book.name, "category_id": book.category_id.id, "status": book.book_status, "image": book.images})
    return result