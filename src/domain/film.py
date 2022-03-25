import datetime
from pydantic import BaseModel, validator, Field
from bson import ObjectId
from src.domain.validators import PyObjectId


class Film(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    genre: str = None
    viewed: bool = False
    mark: int = 0
    comments: str = None
    user_id: str = None
    created_at: datetime.datetime = None
    updated_at: datetime.datetime = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class FilmRequest(BaseModel):
    name: str
    genre: str = None
    viewed: bool = False
    mark: int = 0
    comments: str = None
    user_id: str = None
