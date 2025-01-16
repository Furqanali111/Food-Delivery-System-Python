from fastapi import FastAPI
from Routes import orderRoutes
from Model import model
from DatabaseConfig.databaseConfig import engine

app= FastAPI()

app.include_router(orderRoutes.router)

model.Base.metadata.create_all(engine)