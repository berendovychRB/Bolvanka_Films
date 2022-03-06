from fastapi import FastAPI
from endpoints.film import film_router


app = FastAPI()

app.include_router(film_router)
