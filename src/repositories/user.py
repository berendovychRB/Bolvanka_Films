from bson import ObjectId
from config.database import db

from domain.user import User


class UserNotFoundError(Exception):
    pass


class UserRepository:

    def __init__(self):
        self.db = db.user

    def _get_user_by_id(self, id):
        user = self.db.find_one({"_id": ObjectId(id)})
        if not user:
            raise UserNotFoundError()
        user['id'] = str(user['_id'])
        del (user['_id'])
        return user

    def _get_user_by_username(self, username: str):
        user = self.db.find_one({"username": username})
        if not user:
            raise UserNotFoundError()
        user['id'] = str(user['_id'])
        del (user['_id'])
        return user

    async def get(self, id: str) -> User:
        return self._get_user_by_id(id)

    async def save(self, user: dict) -> User:
        self.db.insert_one(user)
        user = User(**user)
        return user

    async def delete(self, id: str) -> None:
        self.db.find_one_and_delete({"_id": ObjectId(id)})