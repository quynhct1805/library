from fastapi import Depends, FastAPI
from routers import users, books, categories
app = FastAPI()
app.include_router(users.router)
app.include_router(books.router)
app.include_router(categories.router)
# app.include_router(
#     tags=["admin"],
#     responses={418: {"description": "I'm a teapot"}},
# )

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}