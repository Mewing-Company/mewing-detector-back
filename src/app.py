from fastapi import FastAPI
from controllers.image import router

app = FastAPI()

app.include_router(router)