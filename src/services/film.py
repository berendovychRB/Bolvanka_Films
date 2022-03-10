from domain.film import Film, FilmRequest
from repositories.film import FilmRepository


class FilmAlreadyExistsError(Exception):
    pass


class FilmService:

    def __init__(self):
        self.film_repository = FilmRepository()

    async def find(self):
        return await self.film_repository.find()

    async def get(self, id: str):
        return await self.film_repository.get(id)

    async def get_by_name(self, name: str):
        return await self.film_repository.get_by_name(name)

    async def create(self, film: FilmRequest):
        film_data = dict(film)
        if self.film_repository.check_existing_film(name=film_data["name"]):
            raise FilmAlreadyExistsError()
        return await self.film_repository.save(film_data)

    async def update(self, id: str, film: FilmRequest):
        film = Film(name=film.name,
                    genre=film.genre,
                    mark=film.mark,
                    comments=film.comments)
        return await self.film_repository.update(id, film)

    async def delete(self, id: str):
        await self.film_repository.delete(id)
