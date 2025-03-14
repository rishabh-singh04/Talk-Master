from fastapi import FastAPI
from .models import models
from .schemas import schemas

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}