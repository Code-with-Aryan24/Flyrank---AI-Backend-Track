# 📌 Task API – FastAPI CRUD Application

A simple RESTful CRUD API built using **FastAPI** as part of the **FlyRank Backend Internship – Week 2 (Assignment A1)**.

This project demonstrates the implementation of a Task Management API using in-memory storage. The API supports creating, reading, updating, and deleting tasks while following REST principles.

---

## 🚀 Features

- Create new tasks
- View all tasks
- View a task by ID
- Update an existing task
- Delete a task
- Input validation using Pydantic
- Proper HTTP status codes
- Interactive Swagger Documentation

---

## 🛠 Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic

---

## 📁 Project Structure

```
task-api/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Code-with-Aryan24/Flyrank---AI-Backend-Track.git
```

Move inside the project

```bash
cd Flyrank---AI-Backend-Track/task-api
```

Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Project

```bash
python -m uvicorn main:app --reload
```

The API will run at

```
http://127.0.0.1:8000
```

---

## 📖 Swagger Documentation

Interactive API documentation is available at

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | / | API Information |
| GET | /health | Health Check |
| GET | /tasks | Get All Tasks |
| GET | /tasks/{id} | Get Task By ID |
| POST | /tasks | Create Task |
| PUT | /tasks/{id} | Update Task |
| DELETE | /tasks/{id} | Delete Task |

---

## 📤 Sample Request

### Create Task

POST `/tasks`

```json
{
    "title": "Learn FastAPI"
}
```

### Response

```json
{
    "id": 4,
    "title": "Learn FastAPI",
    "done": false
}
```

---

## 📥 Sample Update

PUT `/tasks/4`

```json
{
    "title": "Learn FastAPI Completely",
    "done": true
}
```

---

## 📊 HTTP Status Codes

| Code | Meaning |
|------|---------|
|200|Success|
|201|Resource Created|
|204|Deleted Successfully|
|400|Invalid Request|
|404|Task Not Found|

---

## 🎯 Assignment Objective

This project was developed as part of the **FlyRank Backend Internship Week 2 Assignment**, focusing on:

- REST API Development
- CRUD Operations
- FastAPI Fundamentals
- HTTP Methods
- Request Validation
- Swagger Documentation

---

## 👨‍💻 Author

**Aryan Pandey**

GitHub:
https://github.com/Code-with-Aryan24
