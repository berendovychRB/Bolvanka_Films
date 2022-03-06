from domain.film import Film, FilmRequest
from repositories.film import FilmRepository


class FilmService:

    @staticmethod
    async def find():
        return await FilmRepository.find()

    @staticmethod
    async def get(id: str):
        return await FilmRepository.get(id)

    @staticmethod
    async def create(film: FilmRequest):
        film = Film(name=film.name,
                    genre=film.genre,
                    mark=film.mark,
                    comments=film.comments)
        return await FilmRepository.save(film)

    @staticmethod
    async def update(id: str, film: FilmRequest):
        film = Film(name=film.name,
                    genre=film.genre,
                    mark=film.mark,
                    comments=film.comments)
        return await FilmRepository.update(id, film)

    @staticmethod
    async def delete(id: str):
        await FilmRepository.delete(id)
