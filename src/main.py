from fastapi import FastAPI
from src.endpoints.film import film_router
from src.endpoints.user import user_router


app = FastAPI()

app.include_router(film_router)
app.include_router(user_router)
