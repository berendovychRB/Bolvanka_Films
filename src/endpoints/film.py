from fastapi import APIRouter, Depends, HTTPException

from src.domain.film import FilmRequest
from src.repositories.film import FilmNotFoundError
from src.services.film import FilmAlreadyExistsError, FilmService

film_router = APIRouter(prefix="/films", tags=["Films"])


@film_router.get("/", summary="Retrieve a list of films")
async def all_films(
    service: FilmService = Depends(), parameter: str = None, query: str = None
):
    """
    Retrieve a list of films.

    Search is possible using the `parameter= & query=` parameters.
    ex: `/films/?parameter=viewed&q=True`
    will return all viewed films
    """
    return await service.find(p=parameter, q=query)


@film_router.get("/{user_id}", summary="Retrieve a list of films by user id")
async def all_films_by_user_id(
    user_id: str,
    service: FilmService = Depends(),
    parameter: str = None,
    query: str = None,
):
    """
    Retrieve a list of user's films.

    Search is possible using the `parameter= & query=` parameters.
    ex: `/films/?parameter=viewed&q=True`
    will return all viewed films
    """
    return await service.find_all_by_user_id(user_id, parameter, query)


@film_router.get("/{id}", summary="Retrieve a film by id")
async def get_film_by_id(id: str, service: FilmService = Depends()):
    try:
        film = await service.get(id)
    except FilmNotFoundError:
        raise HTTPException(status_code=404, detail="Film not found")
    return film


@film_router.get("/by_name/{name}", summary="Retrieve a film by name")
async def get_film_by_name(name: str, service: FilmService = Depends()):
    try:
        film = await service.get_by_name(name)
    except FilmNotFoundError:
        raise HTTPException(status_code=404, detail="Film not found")
    return film


@film_router.post("/", summary="Save a film")
async def create_film(film: FilmRequest, service: FilmService = Depends()):
    try:
        film = await service.create(film)
    except FilmAlreadyExistsError:
        raise HTTPException(status_code=409, detail="Film already exists")
    return film


@film_router.patch("/{id}", summary="Update the film")
async def update_film(
    id: str, film: FilmRequest, service: FilmService = Depends()
):
    return await service.update(id, film)


@film_router.patch(
    "/{user_id}/{name}/{mark}", summary="Update the film by name and user id"
)
async def update_film_by_name_and_user_id(
    user_id: str, name: str, mark: int, service: FilmService = Depends()
):
    return await service.update_by_name_and_user_id(
        name=name, user_id=user_id, mark=mark
    )


@film_router.put("/{id}", summary="Update film viewing")
async def update_film_viewing(id: str, service: FilmService = Depends()):
    return await service.update_viewing(id)


@film_router.delete("/{id}", summary="Delete the film")
async def delete_film(id: str, service: FilmService = Depends()):
    await service.delete(id)
    return {"status": "ok"}


@film_router.delete("/{user_id}/{name}", summary="Delete the film by for user")
async def delete_film_by_parameters(
    user_id: str, name: str, service: FilmService = Depends()
):
    await service.delete_by_name_and_user_id(name=name, user_id=user_id)
    return {"status": "ok"}
