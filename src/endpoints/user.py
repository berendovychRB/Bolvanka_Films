from fastapi import APIRouter, Depends, HTTPException

from src.domain.user import UserRequest
from src.services.user import UserService, UserAlreadyExistsError
from src.repositories.user import UserNotFoundError

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/", summary="Retrieve a list of users")
async def all_films(service: UserService = Depends()):
    return await service.find()


@user_router.get("/{id}", summary="Retrieve a user by id")
async def get_user_by_id(id: str, service: UserService = Depends()):
    try:
        user = await service.get(id)
    except UserNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Film not found"
        )
    return user


@user_router.post("/", summary="Save a user")
async def create_film(user: UserRequest, service: UserService = Depends()):
    try:
        user = await service.create(user)
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail="User already exists"
        )
    return user


@user_router.delete("/{id}", summary="Delete the user")
async def delete_film(id: str, service: UserService = Depends()):
    await service.delete(id)
    return {"status": "ok"}