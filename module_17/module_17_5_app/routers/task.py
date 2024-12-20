from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User, Task
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete, values

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task


@router.post("/create")
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    new_task = Task(
        title=task.title,
        content=task.content,
        priority=task.priority,
        user_id=user.id
    )
    db.execute(
        insert(Task).values(
            title=new_task.title,
            content=new_task.content,
            priority=new_task.priority,
            user_id=new_task.user_id
        )
    )
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{task_id}")
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if existing_task:
        db.execute(
            update(Task).where(Task.id == task_id).values(
                title=task.title,
                content=task.content,
                priority=task.priority
            )
        )
        db.commit()
        return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}
    else:
        raise HTTPException(status_code=404, detail="Task was not found")


@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.scalar(select(Task).where(Task.id == task_id))
    if existing_task:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {"status_code": status.HTTP_200_OK, "transaction": "Task delete is successful!"}
    else:
        raise HTTPException(status_code=404, detail="Task was not found")