from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

from db import (
    get_all_tasks,
    get_task,
    create_task,
    update_task,
    delete_task,
)

app = FastAPI(
    title="Task API",
    description="A simple CRUD API using PostgreSQL",
    version="2.0"
)


# -----------------------------
# Request Models
# -----------------------------
class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str
    done: bool


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    return {
        "name": "Task API",
        "database": "PostgreSQL",
        "version": "2.0"
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# -----------------------------
# Get All Tasks
# -----------------------------
@app.get("/tasks")
def read_tasks():
    return get_all_tasks()


# -----------------------------
# Get Task by ID
# -----------------------------
@app.get("/tasks/{task_id}")
def read_task(task_id: int):

    task = get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    return task


# -----------------------------
# Create Task
# -----------------------------
@app.post("/tasks", status_code=201)
def add_task(task: TaskCreate):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    return create_task(task.title)


# -----------------------------
# Update Task
# -----------------------------
@app.put("/tasks/{task_id}")
def edit_task(task_id: int, task: TaskUpdate):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    updated = update_task(
        task_id,
        task.title,
        task.done
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    return updated


# -----------------------------
# Delete Task
# -----------------------------
@app.delete("/tasks/{task_id}", status_code=204)
def remove_task(task_id: int):

    deleted = delete_task(task_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    return Response(status_code=204)