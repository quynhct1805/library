from fastapi import APIRouter
from models.categories import Categories
from pydantic import BaseModel

router = APIRouter()

class DataCategory(BaseModel):
    code: str
    name: str
    description: str = None

@router.get("/api/categories/", tags=["categories"])
async def read_categories():
    categories = Categories.select()
    result = []
    for category in categories:
        result.append({"code": category.code, "name" : category.name, "description": category.description})
    return (result)


@router.get("/api/categories/{category_id}", tags=["categories"])
async def read_categories(category_id):
    categories = Categories.select().where(Categories.id == category_id)
    for category in categories:
        return({"code": category.code, "name" : category.name})



@router.post("/api/categories/", tags=["categories"], status_code=200)
async def create_category(category: DataCategory):
    # print(category)
    Categories.insert(code=category.code, name=category.name, description=category.description).execute()
    return "create category"


@router.patch("/api/categories/{category_code}", tags=["categories"], status_code=200)
async def update_category(category_code: str, category: DataCategory):
    print(category)
    Categories.update(**category.dict()).where(Categories.code == category_code).execute()
    return "update category"
