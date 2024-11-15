from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Создаем объект Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Список пользователей
users = []


# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int


# Главная страница, отображающая всех пользователей
@app.get("/", response_class=HTMLResponse)
def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


# GET запрос для получения конкретного пользователя
@app.get("/user/{user_id}", response_class=HTMLResponse)
def get_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
def create_user(username: str, age: int):
    new_id = 1 if not users else users[-1].id + 1  # Находим новый ID
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


# Заполнение списка пользователей
@app.on_event("startup")
def startup_event():
    create_user("UrbanUser", 24)
    create_user("UrbanTest", 22)
    create_user("Capybara", 60)