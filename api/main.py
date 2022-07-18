from fastapi import FastAPI
from routers import users, books, categories, borrow_histories,authors, reviews
app = FastAPI()
app.include_router(users.router)
app.include_router(books.router)
app.include_router(categories.router)
app.include_router(borrow_histories.router)
app.include_router(authors.router)
app.include_router(reviews.router)
# app.include_router(
#     tags=["admin"],
#     responses={418: {"description": "I'm a teapot"}},
# )

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}