import sqlite3
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing tasks.",
    version="1.0"
)
# -----------------------------
# SQLite Database Connection
# -----------------------------
connection = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = connection.cursor()

# -----------------------------
# Create Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL
)
""")

connection.commit()

# -----------------------------
# Seed Initial Data
# -----------------------------
cursor.execute("SELECT COUNT(*) FROM tasks")

count = cursor.fetchone()[0]

if count == 0:

    sample_tasks = [
        ("Learn FastAPI", False),
        ("Complete FlyRank Assignment", False),
        ("Push code to GitHub", False)
    ]

    cursor.executemany(
        "INSERT INTO tasks(title, done) VALUES (?, ?)",
        sample_tasks
    )

    connection.commit()

# -----------------------------
# In-memory database
# (Keep this until Stage 1)
# -----------------------------
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Complete FlyRank Assignment",
        "done": False
    },
    {
        "id": 3,
        "title": "Push code to GitHub",
        "done": False
    }
]

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
@app.get("/", summary="API Information")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": [
            "/tasks"
        ]
    }


# -----------------------------
# Health Endpoint
# -----------------------------
@app.get("/health", summary="Health Check")
def health():
    return {
        "status": "ok"
    }


# -----------------------------
# Get All Tasks
# -----------------------------
@app.get("/tasks", summary="Get all tasks")
def get_tasks():
    return tasks


# -----------------------------
# Get Task By ID
# -----------------------------
@app.get("/tasks/{task_id}", summary="Get task by ID")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )


# -----------------------------
# Create Task
# -----------------------------
@app.post("/tasks", status_code=201, summary="Create a new task")
def create_task(task: TaskCreate):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task


# -----------------------------
# Update Task
# -----------------------------
@app.put("/tasks/{task_id}", summary="Update an existing task")
def update_task(task_id: int, updated_task: TaskUpdate):

    if updated_task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    for task in tasks:

        if task["id"] == task_id:

            task["title"] = updated_task.title
            task["done"] = updated_task.done

            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )


# -----------------------------
# Delete Task
# -----------------------------
@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            return Response(status_code=204)

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )