import datetime
from typing import List

from bson import ObjectId

from src.config.database import db
from src.domain.film import Film


class FilmNotFoundError(Exception):
    pass


class FilmRepository:
    def __init__(self):
        self.db = db.films

    def _get_item_by_id(self, id):
        film = self.db.find_one({"_id": ObjectId(id)})
        if not film:
            raise FilmNotFoundError()
        film["id"] = str(film["_id"])
        del film["_id"]
        return film

    def _get_item_by_name(self, name: str):
        film = self.db.find_one({"name": name})
        if not film:
            raise FilmNotFoundError()
        film["id"] = str(film["_id"])
        del film["_id"]
        return film

    def check_existing_film(self, name: str, user_id: str):
        film = self.db.find_one({"name": name, "user_id": user_id})
        if film:
            return True
        return False

    def _update(self, id, data):
        query = {"_id": ObjectId(id)}
        values = {"$set": data}
        self.db.update_one(query, values)

    async def find(self, p, q) -> List[Film]:
        films = []
        if p and q:
            if q == "True":
                q = True
            else:
                q = False
            for film in self.db.find({p: q}):
                films.append(Film(**film))
        else:
            for film in self.db.find():
                films.append(Film(**film))
        return films

    async def find_all_by_user_id(self, user_id, p, q) -> List[Film]:
        films = []
        if p and q:
            if q == "True":
                q = True
            else:
                q = False
            for film in self.db.find({"user_id": user_id, p: q}):
                films.append(Film(**film))
        else:
            for film in self.db.find({"user_id": user_id}):
                films.append(Film(**film))
        return films

    async def get(self, id: str) -> Film:
        return self._get_item_by_id(id)

    async def get_by_name(self, name: str) -> Film:
        return self._get_item_by_name(name)

    async def save(self, film: dict) -> Film:
        film["created_at"] = datetime.datetime.now()
        film["updated_at"] = datetime.datetime.now()
        self.db.insert_one(film)
        film = Film(**film)
        return film

    async def update(self, id: str, film: Film) -> Film:
        stored_data = self._get_item_by_id(id)
        input_data = film.dict()
        del input_data["created_at"]
        for key, value in input_data.items():
            stored_data[key] = value
        stored_data["updated_at"] = datetime.datetime.now()
        self._update(id, stored_data)
        film = self._get_item_by_id(id)
        return film

    async def update_by_name_and_user_id(
        self, name: str, user_id: str, mark: int
    ):
        film = self.db.find_one({"name": name, "user_id": user_id})
        if not film:
            raise FilmNotFoundError()
        film["id"] = str(film["_id"])
        del film["_id"]
        film["mark"] = mark
        film["viewed"] = True
        film["updated_at"] = datetime.datetime.now()
        self._update(film["id"], film)
        film = self._get_item_by_id(film["id"])
        return film

    async def update_viewing(self, id: str) -> Film:
        stored_film = self._get_item_by_id(id)
        stored_film["viewed"] = not stored_film["viewed"]
        self._update(id, stored_film)
        film = self._get_item_by_id(id)
        return film

    async def delete(self, id: str) -> None:
        self.db.find_one_and_delete({"_id": ObjectId(id)})

    async def delete_by_name_and_user_id(
        self, name: str, user_id: str
    ) -> None:
        self.db.find_one_and_delete({"name": name, "user_id": user_id})
