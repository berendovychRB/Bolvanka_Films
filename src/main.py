from fastapi import FastAPI
from endpoints.film import film_router
from endpoints.user import user_router


app = FastAPI()

app.include_router(film_router)
app.include_router(user_router)
