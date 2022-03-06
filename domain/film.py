import datetime
from pydantic import BaseModel, validator


class Film(BaseModel):
    name: str
    genre: str = None
    mark: int
    comments: str = None
    created_at: datetime.datetime = None
    updated_at: datetime.datetime = None

    @validator("created_at", pre=True, always=True)
    def set_created_to_now(cls, v):
        return v or datetime.datetime.now()

    @validator("updated_at", pre=True, always=True)
    def set_updated_to_now(cls, v):
        return v or datetime.datetime.now()


class FilmRequest(BaseModel):
    name: str
    genre: str = None
    mark: int
    comments: str = None

# ГЛЯНУТИ В МЕДІАТУЛ ТАМ В АПЛІКЕЙШН Є СПОСІБ!!!!