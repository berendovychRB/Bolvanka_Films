from fastapi import APIRouter, Depends, HTTPException

from domain.user import UserRequest
from services.user import UserService
from repositories.user import UserNotFoundError

user_router = APIRouter(prefix="/users", tags=["Users"])


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
    user = await service.create(user)
    return user


@user_router.delete("/{id}", summary="Delete the user")
async def delete_film(id: str, service: UserService = Depends()):
    await service.delete(id)
    return {"status": "ok"}