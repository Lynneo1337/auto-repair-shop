from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models

app = FastAPI(
    title="Автомастерская API",
    description="Система управления автосервисом",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Добро пожаловать в Автомастерскую!",
        "status": "Сервер работает"
    }


@app.get("/health")
async def health_check():
    return {"status": "OK", "data": "Сервер жив и готов к работе"}


@app.get("/clients/{client_id}")
async def get_client(client_id: int):
    return {
        "id": client_id,
        "name": "Иванов Иван Иванович",
        "phone": "+7 (999) 123-45-67",
        "discount": 10
    }

models.Base.metadata.create_all(bind=engine)