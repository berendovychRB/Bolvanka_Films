from src.domain.user import UserRequest
from src.repositories.user import UserRepository


class UserAlreadyExistsError(Exception):
    pass


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def find(self):
        return await self.user_repository.find()

    async def get(self, id: str):
        return await self.user_repository.get(id)

    async def create(self, user: UserRequest):
        user_data = dict(user)
        if self.user_repository.check_existing_user(
            telegram_id=user_data["telegram_id"]
        ):
            raise UserAlreadyExistsError()
        return await self.user_repository.save(user_data)

    async def delete(self, id: str):
        await self.user_repository.delete(id)
