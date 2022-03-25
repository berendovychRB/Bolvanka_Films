from src.domain.film import Film, FilmRequest
from src.repositories.film import FilmRepository


class FilmAlreadyExistsError(Exception):
    pass


class FilmService:
    def __init__(self):
        self.film_repository = FilmRepository()

    async def find(self, p, q):
        return await self.film_repository.find(p, q)

    async def find_all_by_user_id(self, user_id: str, p, q):
        return await self.film_repository.find_all_by_user_id(user_id, p, q)

    async def get(self, id: str):
        return await self.film_repository.get(id)

    async def get_by_name(self, name: str):
        return await self.film_repository.get_by_name(name)

    async def create(self, film: FilmRequest):
        film_data = dict(film)
        if self.film_repository.check_existing_film(
            name=film_data["name"], user_id=film_data["user_id"]
        ):
            raise FilmAlreadyExistsError()
        return await self.film_repository.save(film_data)

    async def update(self, id: str, film: FilmRequest):
        film = Film(
            name=film.name,
            genre=film.genre,
            mark=film.mark,
            comments=film.comments,
            user_id=film.user_id,
        )
        return await self.film_repository.update(id, film)

    async def update_by_name_and_user_id(
        self, name: str, user_id: str, mark: int
    ):
        return await self.film_repository.update_by_name_and_user_id(
            name, user_id, mark
        )

    async def update_viewing(self, id: str):
        return await self.film_repository.update_viewing(id)

    async def delete(self, id: str):
        await self.film_repository.delete(id)

    async def delete_by_name_and_user_id(self, name: str, user_id: str):
        await self.film_repository.delete_by_name_and_user_id(name, user_id)
