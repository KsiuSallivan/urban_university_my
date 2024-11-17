from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router
from sqlalchemy import create_engine
from module_17.module_17_2_app.backend.db import Base

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)


# Создание движка базы данных
DATABASE_URL = 'sqlite:///taskmanager.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Вывод SQL-запроса в консоль
print(Base.metadata.tables)