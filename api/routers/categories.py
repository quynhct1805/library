from fastapi import APIRouter
from models.categories import Categories

router = APIRouter()


@router.get("/api/categories/", tags=["categories"])
async def read_categories():
    categories = Categories.select()
    result = []
    for category in categories:
        result.append({"id": category.id, "name" : category.name})
    return (result)


@router.post("/categories/", tags=["categories"])
async def create_category():
    category = Categories.create(name="Triết học - Tâm lý")