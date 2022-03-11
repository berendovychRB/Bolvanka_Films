import datetime
from typing import List

from bson import ObjectId
from config.database import db

from domain.user import User


class UserNotFoundError(Exception):
    pass


class UserRepository:

    def __init__(self):
        self.db = db.users

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

    def check_existing_user(self, telegram_id):
        user = self.db.find_one({"telegram_id": telegram_id})
        if user:
            return True
        return False

    async def find(self) -> List[User]:
        users = []
        for user in self.db.find():
            users.append(User(**user))
        return users

    async def get(self, id: str) -> User:
        return self._get_user_by_id(id)

    async def save(self, user: dict) -> User:
        user["created_at"] = datetime.datetime.now()
        self.db.insert_one(user)
        user = User(**user)
        return user

    async def delete(self, id: str) -> None:
        self.db.find_one_and_delete({"_id": ObjectId(id)})