from fastapi import FastAPI
from Routes import orderRoutes

app= FastAPI()

app.include_router(orderRoutes.router)
