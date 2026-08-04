import os

import psycopg
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to PostgreSQL
connection = psycopg.connect(DATABASE_URL)

connection.autocommit = True

cursor = connection.cursor()

# -----------------------------
# Create Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL
)
""")

# -----------------------------
# Seed Initial Data
# -----------------------------
cursor.execute("SELECT COUNT(*) FROM tasks")

count = cursor.fetchone()[0]

if count == 0:

    cursor.executemany(
        "INSERT INTO tasks(title, done) VALUES (%s, %s)",
        [
            ("Learn FastAPI", False),
            ("Complete FlyRank Assignment", False),
            ("Push code to GitHub", False)
        ]
    )