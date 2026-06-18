import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import engine, Base
from routers import promos

# 1. Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

# 2. Создание таблиц в БД
Base.metadata.create_all(bind=engine)

# 3. Создание приложения — СНАЧАЛА создаём app
app = FastAPI(
    title="Promo Manager",
    description="API для управления промокодами",
    version="1.0.0"
)

# 4. Только ПОСЛЕ этого используем app
app.mount("/static", StaticFiles(directory="."), name="static")

app.include_router(promos.router)

@app.get("/")
def frontend():
    return FileResponse("promo_manager_frontend.html")