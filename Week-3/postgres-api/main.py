import sqlite3
from db import connection, cursor
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

    cursor.execute("SELECT id, title, done FROM tasks ORDER BY id")

    rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "title": row[1],
            "done": row[2]
        }
        for row in rows
    ]


# -----------------------------
# Get Task By ID
# -----------------------------
@app.get("/tasks/{task_id}", summary="Get task by ID")
def get_task(task_id: int):

    cursor.execute(
        "SELECT id, title, done FROM tasks WHERE id = %s",
        (task_id,)
    )

    row = cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }


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

    cursor.execute(
        "INSERT INTO tasks(title, done) VALUES(?, ?)",
        (task.title, False)
    )

    connection.commit()

    new_id = cursor.lastrowid

    return {
        "id": new_id,
        "title": task.title,
        "done": False
    }


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

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    if cursor.fetchone() is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    cursor.execute(
        """
        UPDATE tasks
        SET title = ?, done = ?
        WHERE id = ?
        """,
        (updated_task.title, updated_task.done, task_id)
    )

    connection.commit()

    return {
        "id": task_id,
        "title": updated_task.title,
        "done": updated_task.done
    }


# -----------------------------
# Delete Task
# -----------------------------
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    if cursor.fetchone() is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    return Response(status_code=204)