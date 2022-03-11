from fastapi import APIRouter, Depends, HTTPException

from domain.film import FilmRequest
from services.film import FilmService, FilmAlreadyExistsError
from repositories.film import FilmNotFoundError

film_router = APIRouter(prefix="/films")


@film_router.get("/")
async def all_films(service: FilmService = Depends()):
    return await service.find()


@film_router.get("/{id}")
async def get_film_by_id(id: str, service: FilmService = Depends()):
    try:
        film = await service.get(id)
    except FilmNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Film not found"
        )
    return film


@film_router.get("/by_name/{name}")
async def get_film_by_name(name: str, service: FilmService = Depends()):
    try:
        film = await service.get_by_name(name)
    except FilmNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Film not found"
        )
    return film


@film_router.post("/")
async def create_film(film: FilmRequest, service: FilmService = Depends()):
    try:
        film = await service.create(film)
    except FilmAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail="Film already exists"
        )
    return film


@film_router.patch("/{id}")
async def update_film(id: str,
                      film: FilmRequest,
                      service: FilmService = Depends()):
    return await service.update(id, film)


@film_router.put("/{id}")
async def update_film_viewing(id: str, service: FilmService = Depends()):
    return await service.update_viewing(id)


@film_router.delete("/{id}")
async def delete_film(id: str, service: FilmService = Depends()):
    await service.delete(id)
    return {"status": "ok"}
