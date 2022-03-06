from fastapi import APIRouter

from domain.film import FilmRequest
from services.film import FilmService


film_router = APIRouter(prefix="/films")


@film_router.get("/")
async def all_films():
    return await FilmService.find()


@film_router.get("/{id}")
async def get_film(id: str):
    return await FilmService.get(id)


@film_router.post("/")
async def create_film(film: FilmRequest):
    return await FilmService.create(film)


@film_router.put("/{id}")
async def update_film(id: str, film: FilmRequest):
    return await FilmService.update(id, film)


@film_router.delete("/{id}")
async def delete_film(id: str):
    await FilmService.delete(id)
    return {"status": "ok"}
