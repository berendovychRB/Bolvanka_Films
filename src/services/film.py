from domain.film import Film, FilmRequest
from repositories.film import FilmRepository


class FilmService:

    def __init__(self):
        self.film_repository = FilmRepository()

    async def find(self):
        return await self.film_repository.find()

    async def get(self, id: str):
        return await self.film_repository.get(id)

    async def create(self, film: FilmRequest):
        film = Film(name=film.name,
                    genre=film.genre,
                    mark=film.mark,
                    comments=film.comments)
        return await self.film_repository.save(film)

    async def update(self, id: str, film: FilmRequest):
        film = Film(name=film.name,
                    genre=film.genre,
                    mark=film.mark,
                    comments=film.comments)
        return await self.film_repository.update(id, film)

    async def delete(self, id: str):
        await self.film_repository.delete(id)
