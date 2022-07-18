from fastapi import APIRouter
from models.authors import Authors
from models.books import Books
from peewee import fn

router = APIRouter()

@router.get("/api/authors/", tags=["authors"])
async def read_authors():
    authors = Authors.select()
    result = []
    for author in authors:
        result.append({"id": author.id, "name": author.name})
    return (result)


@router.get("/api/author/{book_id}", tags=["authors"])
async def read_author(book_id):
    authors = (Authors
                .select(Authors.id,Authors.name)
                .where(Authors.id.in_(Books
                                        .select(fn.unnest(Books.author_ids))
                                        .where(Books.id == book_id)))
                        )
                
    result = []
    for author in authors:
        result.append({"id": author.id, "name": author.name})
    return (result)
