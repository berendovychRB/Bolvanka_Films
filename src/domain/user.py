import datetime
from typing import List

from bson import ObjectId
from pydantic import BaseModel, Field

from src.domain.film import Film
from src.domain.validators import PyObjectId


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    telegram_id: str
    username: str = None
    first_name: str = None
    last_name: str = None
    films: List[Film] = None
    created_at: datetime.datetime = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UserRequest(BaseModel):
    telegram_id: str
    username: str = None
    first_name: str = None
    last_name: str = None
    films: List[Film] = None
