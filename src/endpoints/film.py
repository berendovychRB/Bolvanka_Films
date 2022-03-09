from fastapi import APIRouter, Depends, HTTPException

from domain.film import FilmRequest
from services.film import FilmService
from repositories.film import FilmNotFoundError


film_router = APIRouter(prefix="/films")


@film_router.get("/")
async def all_films(service: FilmService = Depends()):
    return await service.find()


@film_router.get("/{id}")
async def get_film(id: str, service: FilmService = Depends()):
    try:
        film = await service.get(id)
    except FilmNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Film not found"
        )
    return film


@film_router.post("/")
async def create_film(film: FilmRequest, service: FilmService = Depends()):
    return await service.create(film)


@film_router.patch("/{id}")
async def update_film(id: str,
                      film: FilmRequest,
                      service: FilmService = Depends()):
    return await service.update(id, film)


@film_router.delete("/{id}")
async def delete_film(id: str, service: FilmService = Depends()):
    await service.delete(id)
    return {"status": "ok"}
