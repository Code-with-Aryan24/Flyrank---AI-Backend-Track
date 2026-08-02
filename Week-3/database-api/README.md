# 📌 Task API with SQLite – FlyRank Backend Internship (Week 3)

A RESTful CRUD API built using **FastAPI** and **SQLite** as part of the **FlyRank AI Backend Internship – Week 3 Assignment**.

This project upgrades the Week 2 Task API by replacing the in-memory Python list with a SQLite database, enabling persistent storage while keeping the API endpoints unchanged.

---

# 🚀 Features

- Create a new task
- View all tasks
- View a task by ID
- Update an existing task
- Delete a task
- Persistent storage using SQLite
- Input validation using Pydantic
- Interactive Swagger UI
- Proper HTTP status codes
- Parameterized SQL queries

---

# 🛠️ Tech Stack

- Python 3.12
- FastAPI
- SQLite
- sqlite3
- Uvicorn
- Pydantic

---

# 📂 Project Structure

```
database-api/
│
├── main.py
├── tasks.db
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

---

# 💾 Why SQLite?

SQLite is a lightweight relational database that stores all data inside a single `.db` file.

For this assignment it is used because:

- No installation required
- Built into Python
- Easy to learn SQL
- Persistent storage
- Perfect for small backend applications

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Code-with-Aryan24/Flyrank---AI-Backend-Track.git
```

Navigate to the project

```bash
cd Flyrank---AI-Backend-Track/Week-3/database-api
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python -m uvicorn main:app --reload
```

The API runs at:

```
http://127.0.0.1:8000
```

---

# 📖 Swagger Documentation

Open:

```
http://127.0.0.1:8000/docs
```

Use **Try it out** to test all CRUD operations.

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | / | API Information |
| GET | /health | Health Check |
| GET | /tasks | Get All Tasks |
| GET | /tasks/{id} | Get Task By ID |
| POST | /tasks | Create New Task |
| PUT | /tasks/{id} | Update Task |
| DELETE | /tasks/{id} | Delete Task |

---

# 📤 Sample POST Request

```json
{
    "title": "Learn SQLite"
}
```

### Response

```json
{
    "id": 4,
    "title": "Learn SQLite",
    "done": false
}
```

---

# 📥 Sample PUT Request

```json
{
    "title": "Learn SQLite Completely",
    "done": true
}
```

---

# 🗃️ Example SQL Query

```sql
SELECT * FROM tasks;
```

Other useful queries:

```sql
SELECT * FROM tasks WHERE done = 1;
```

```sql
SELECT COUNT(*) FROM tasks;
```

---

# 📸 Database Screenshot

Create a folder named `screenshots`.

```
database-api/
│
└── screenshots/
    └── database.png
```

Open **DB Browser for SQLite**, take a screenshot of the `tasks` table, and add it below.

```markdown
## Database

![Database](screenshots/database.png)
```

---

# 📸 Swagger Screenshot

Take a screenshot of the Swagger UI and save it as:

```
screenshots/swagger.png
```

Add:

```markdown
## Swagger UI

![Swagger](screenshots/swagger.png)
```

---

# 📦 Automatic Database Creation

The application automatically:

- Creates `tasks.db`
- Creates the `tasks` table if it does not exist
- Inserts three sample tasks on the first run only

No manual database setup is required.

---

# ✅ HTTP Status Codes

| Code | Meaning |
|------|---------|
|200|OK|
|201|Created|
|204|No Content|
|400|Bad Request|
|404|Not Found|

---

# 🎯 Learning Outcomes

Through this assignment I learned:

- FastAPI CRUD APIs
- SQLite integration
- SQL (SELECT, INSERT, UPDATE, DELETE)
- Parameterized SQL queries
- Database persistence
- REST API design
- Swagger documentation

---

# 👨‍💻 Author

**Aryan Pandey**

GitHub: https://github.com/Code-with-Aryan24