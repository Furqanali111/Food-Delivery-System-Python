from fastapi import FastAPI
from Routes import restaurantRoutes

app= FastAPI()

app.include_router(orderRoutes.router)
