from repositories.user import UserRepository
from domain.user import UserRequest


class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    async def find(self):
        return await self.user_repository.find()

    async def get(self, id: str):
        return await self.user_repository.get(id)

    async def create(self, user: UserRequest):
        film_data = dict(user)
        return await self.user_repository.save(film_data)

    async def delete(self, id: str):
        await self.user_repository.delete(id)
