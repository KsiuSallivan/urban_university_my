from typing import Annotated

from fastapi import FastAPI, HTTPException, Path

app = FastAPI()

# Изначальный словарь пользователей
users = {'1': 'Имя: Example, возраст: 18'}


# GET запрос для получения всех пользователей
@app.get("/users")
def get_users():
    return users


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
def create_user(
        username: Annotated[str, Path(
            min_length=5, max_length=20, description="Enter username"
        )],
        age: Annotated[int, Path(
            ge=18, le=120, description="Enter age"
        )]
):
    new_id = str(max(map(int, users.keys())) + 1)  # Находим максимальный ID и увеличиваем на 1
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


# PUT запрос для обновления пользователя
@app.put("/user/{user_id}/{username}/{age}")
def update_user(
        user_id: Annotated[int, Path(
        ge=1, le=100, description="Enter User ID")],
        username: Annotated[str, Path(
            min_length=5, max_length=20, description="Enter username"
        )],
        age: Annotated[int, Path(
            ge=18, le=120, description="Enter age"
        )]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
def delete_user(
        user_id: Annotated[int, Path(
        ge=1, le=100, description="Enter User ID")]):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"
