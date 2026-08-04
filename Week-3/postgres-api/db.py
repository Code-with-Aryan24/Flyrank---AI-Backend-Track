import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg.connect(DATABASE_URL)
connection.autocommit = True

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL
)
""")

cursor.execute("SELECT COUNT(*) FROM tasks")

count = cursor.fetchone()[0]

if count == 0:

    cursor.executemany(
        """
        INSERT INTO tasks(title, done)
        VALUES(%s,%s)
        """,
        [
            ("Learn FastAPI", False),
            ("Complete FlyRank Assignment", False),
            ("Push code to GitHub", False)
        ]
    )


def get_all_tasks():

    cursor.execute("""
    SELECT id,title,done
    FROM tasks
    ORDER BY id
    """)

    rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "title": row[1],
            "done": row[2]
        }
        for row in rows
    ]


def get_task(task_id):

    cursor.execute(
        """
        SELECT id,title,done
        FROM tasks
        WHERE id=%s
        """,
        (task_id,)
    )

    row = cursor.fetchone()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }


def create_task(title):

    cursor.execute(
        """
        INSERT INTO tasks(title,done)
        VALUES(%s,%s)
        RETURNING id,title,done
        """,
        (title, False)
    )

    row = cursor.fetchone()

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }


def update_task(task_id, title, done):

    cursor.execute(
        """
        UPDATE tasks
        SET title=%s,
            done=%s
        WHERE id=%s
        RETURNING id,title,done
        """,
        (title, done, task_id)
    )

    row = cursor.fetchone()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }


def delete_task(task_id):

    cursor.execute(
        """
        DELETE FROM tasks
        WHERE id=%s
        RETURNING id
        """,
        (task_id,)
    )

    return cursor.fetchone()