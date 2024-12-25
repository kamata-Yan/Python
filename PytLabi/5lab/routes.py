from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import List, Optional
from models import Task
from database import tasks_db
from email_utils import send_email

router = APIRouter()

@router.post("/", response_model=Task)
def add_task(task: Task, background_tasks: BackgroundTasks):
    if task.id in tasks_db:
        raise HTTPException(status_code=400, detail="Task ID already exists.")
    tasks_db[task.id] = task
    background_tasks.add_task(send_email, task)
    return task

@router.get("/", response_model=List[Task])
def get_tasks(completed: Optional[bool] = None, limit: Optional[int] = None):
    result = [task for task in tasks_db.values() if completed is None or task.completed == completed]
    if limit:
        result = result[:limit]
    return result

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found.")
    tasks_db[task_id] = task
    return task

@router.delete("/{task_id}", response_model=Task)
def delete_task(task_id: int):
    task = tasks_db.pop(task_id, None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task
