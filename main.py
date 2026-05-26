import logging
from fastapi import FastAPI
from database import engine, Base
from routers import promos

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

# Создание таблиц в БД при старте (если не существуют)
Base.metadata.create_all(bind=engine)

# Создание приложения
app = FastAPI(
    title="Promo Manager",
    description="API для управления промокодами",
    version="1.0.0"
)

# Подключение роутера
app.include_router(promos.router)