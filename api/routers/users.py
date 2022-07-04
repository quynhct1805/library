from fastapi import APIRouter
from models.users import Users

router = APIRouter()


@router.get("/api/users/", tags=["users"])
async def read_users():
    users = Users.select()
    result = []
    for user in users:
        result.append({"id": user.id, "name": user.name, "phone": user.phone, "email": user.email})
    return (result)


@router.get("/users/{user_id}", tags=["users"])
async def read_user(user_id):
    users = Users.select().where(Users.id == user_id)
    for user in users:
        return({"id": user.id, "name": user.name, "phone": user.phone, "email": user.email})
    

@router.post("/users/", tags=["users"])
async def create_user():
    users = Users.create(name="ken2", phone="01555555", email="ken2@gmail.com")