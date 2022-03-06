from typing import List

from bson import ObjectId

from config.database import films_collection
from serializers.film import films_serializer

from domain.film import Film


class FilmRepository:

    @staticmethod
    async def find() -> List[Film]:
        films = films_serializer(films_collection.find())
        return films

    @staticmethod
    async def get(id: str) -> Film:
        films = films_serializer(
            films_collection.find({"_id": ObjectId(id)}))
        return films[0]

    @staticmethod
    async def save(film: Film) -> Film:
        _id = films_collection.insert_one(dict(film))
        film = films_serializer(
            films_collection.find({"_id": _id.inserted_id})
        )
        return film[0]

    @staticmethod
    async def update(id: str, film: Film) -> Film:
        films_collection.find_one_and_update({"_id": ObjectId(id)}, {
            "$set": dict(film)
        })
        films = films_serializer(
            films_collection.find({"_id": ObjectId(id)}))
        return films[0]

    @staticmethod
    async def delete(id: str) -> None:
        films_collection.find_one_and_delete({"_id": ObjectId(id)})
