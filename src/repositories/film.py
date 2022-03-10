from typing import List

from bson import ObjectId

from config.database import db

from domain.film import Film


class FilmNotFoundError(Exception):
    pass


class FilmRepository:

    def __init__(self):
        self.db = db.films

    def _get_item_by_id(self, id):
        film = self.db.find_one({"_id": ObjectId(id)})
        if not film:
            raise FilmNotFoundError()
        film['id'] = str(film['_id'])
        del (film['_id'])
        return film

    def _get_item_by_name(self, name: str):
        film = self.db.find_one({"name": name})
        if not film:
            raise FilmNotFoundError()
        film['id'] = str(film['_id'])
        del (film['_id'])
        return film

    def check_existing_film(self, name: str):
        film = self.db.find_one({"name": name})
        if film:
            return True
        return False

    def _update(self, id, data):
        query = {"_id": ObjectId(id)}
        values = {"$set": data}
        self.db.update_one(query, values)

    async def find(self) -> List[Film]:
        films = []
        for film in self.db.find():
            films.append(Film(**film))
        return films

    async def get(self, id: str) -> Film:
        return self._get_item_by_id(id)

    async def get_by_name(self, name: str) -> Film:
        return self._get_item_by_name(name)

    async def save(self, film: dict) -> Film:
        self.db.insert_one(film)
        film = Film(**film)
        return film

    async def update(self, id: str, film: Film) -> Film:
        stored_data = self._get_item_by_id(id)
        input_data = film.dict()
        for key, value in input_data.items():
            stored_data[key] = value
        del (stored_data["created_at"])
        self._update(id, stored_data)
        film = self._get_item_by_id(id)
        return film

    async def delete(self, id: str) -> None:
        self.db.find_one_and_delete({"_id": ObjectId(id)})
