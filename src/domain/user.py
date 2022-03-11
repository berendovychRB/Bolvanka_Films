import datetime
from typing import List

from pydantic import BaseModel, validator, Field
from bson import ObjectId
from domain.validators import PyObjectId
from domain.film import Film


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    telegram_id: str
    username: str
    first_name: str
    last_name: str
    films: List[Film] = None
    created_at: datetime.datetime = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @validator("created_at", pre=True, always=True)
    def set_created_to_now(cls, v):
        return v or datetime.datetime.now()


class UserRequest(BaseModel):
    telegram_id: str
    username: str
    first_name: str
    last_name: str
    films: List[Film] = None