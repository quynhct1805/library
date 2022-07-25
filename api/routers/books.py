from fastapi import APIRouter
from models.books import Books
from models.borrow_histories import Borrow_histories
from models.reviews import Reviews
from models.authors import Authors
from peewee import fn, JOIN
from pydantic import BaseModel


router = APIRouter()


class DataUpdateBookStatus(BaseModel):
    status: str
class DataBook(BaseModel):
    image: str
    name: str
    publisher: str
    author_ids: list[int]
    category_id: int
    years: int
    pages: int
    fee_per_day: float
    summary: str


@router.get("/api/books/", tags=["books"])
async def read_books():
    books = (Books
                .select(Books.id, Books.name, Books.category_id, Books.book_status, Books.image, 
                        fn.COUNT(Borrow_histories.id).alias('total'), fn.AVG(Reviews.rate_stars).alias('rate'))
                .join(Borrow_histories, JOIN.LEFT_OUTER)
                .switch(Books)
                .join(Reviews, JOIN.LEFT_OUTER)
                .group_by(Books.id))
    result = []
    for book in books:
        result.append({"id": book.id, "name": book.name, "category_id": book.category_id.code, "category_name": book.category_id.name, 
                        "status": book.book_status, "image": book.image, "number_borrow": book.total, "reviews": book.rate})
    return (result)
    

@router.get("/cart/{user_id}", tags=["cart"])
async def read_cart(user_id):
    books = Books.select().where(Books.user_id == user_id)
    result = []
    for book in books:
        result.append({"id": book.id, "name": book.name})
    return (result)


@router.get("/api/book/{book_id}", tags=["books"])
async def read_book(book_id):
    books = (Books
                .select(Books.id, Books.name, Books.category_id, Books.book_status, Books.image, Books.publisher, 
                    Books.years, Books.pages, Books.fee_per_day, Books.summary, Books.due_date,
                    fn.COUNT(Borrow_histories.id.distinct()).alias('total'), fn.AVG(Reviews.rate_stars).alias('rate'))
                .join(Borrow_histories, JOIN.LEFT_OUTER)
                .switch(Books)
                .join(Reviews, JOIN.LEFT_OUTER)
                .where(Books.id == book_id)
                .group_by(Books.id))
    for book in books:
        return({"id": book.id, "name": book.name, "category_name": book.category_id.name, "status": book.book_status, "image" : book.image,
                    "publisher": book.publisher, "year": book.years, "pages": book.pages, "fee": book.fee_per_day, "summary": book.summary,
                    "due_date": book.due_date, "number_borrow": book.total, "reviews": book.rate})


@router.get("/api/books/{category_id}", tags=["books"])
async def read_books(category_id):
    books = (Books
                .select(Books.id, Books.name, Books.category_id, Books.book_status, Books.image, 
                        fn.COUNT(Borrow_histories.id).alias('total'), fn.AVG(Reviews.rate_stars).alias('rate'))
                .join(Borrow_histories, JOIN.LEFT_OUTER)
                .switch(Books)
                .join(Reviews, JOIN.LEFT_OUTER)
                .where(Books.category_id == category_id)
                .group_by(Books.id))
    result = []
    for book in books:
        result.append({"id": book.id, "name": book.name, "category_id": book.category_id.code, "status": book.book_status, 
                        "image": book.image, "number_borrow": book.total, "reviews": book.rate})
    return result
    


@router.patch("/api/book/{book_id}", tags=["books"])
async def update_book(book_id, data: DataUpdateBookStatus):
    print (data)
    book = (Books
                .update(book_status = data)
                .where(Books.id == book_id)
                .execute())


@router.get("/api/user_borrow/{book_id}", tags=["books"])
async def read_book(book_id):
    books = (Books
                .select()
                .where((Books.id == book_id) & (Books.book_status == 'Borrowing')))
    for book in books:
        return({"book_id": book.id, "book_name": book.name, "user": book.user_id.name})


@router.get("/api/admin/books/", tags=["books"])
async def read_books():
    books = (Books
                .select(Books.id, Books.name, Books.category_id, Books.book_status, Books.fee_per_day, fn.ARRAY_AGG(Authors.name).alias('anames'),
                fn.ARRAY_AGG(Authors.id).alias('aids'), Books.image, Books.publisher, Books.years, Books.pages, Books.summary)
                .join(Authors, on=(Authors.id == fn.ANY(Books.author_ids)))
                .group_by(Books.id))
    result = []
    for book in books:
        result.append({"id": book.id, "name": book.name, "category_id": book.category_id.id, "category_name": book.category_id.name, "status": book.book_status,
                        "fee_per_day": book.fee_per_day,"image": book.image, "author_ids": book.aids,"author_names": book.anames, "publisher": book.publisher,
                        "year": book.years, "pages": book.pages, "summary": book.summary})
    return (result)


@router.post("/api/books/", tags=["books"], status_code=200)
async def create_book(book: DataBook):
    # print(book)
    Books.insert(**book.dict()).execute()
    return "create book"
