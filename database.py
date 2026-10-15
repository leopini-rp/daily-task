import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent
DB_NAME = "tasks.db"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "tasks"


def db_init():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
        "("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "task_title TEXT NOT NULL,"
        "task_time TEXT NOT NULL,"
        "completed INTEGER NOT NULL DEFAULT 0 CHECK (completed IN (0, 1))"
        ")"
    )

    connection.commit()
    cursor.close()
    connection.close()


def save_db_item(task_title, task_time):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f"INSERT INTO {TABLE_NAME} (task_title, task_time)"
        "VALUES (?, ?)",
        (task_title, task_time)
    )

    id_ = cursor.lastrowid

    connection.commit()
    cursor.close()
    connection.close()

    return id_


def update_completed(completed, id_):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f"UPDATE {TABLE_NAME} SET completed = ? WHERE id = ?",
        (completed, id_)
    )

    connection.commit()

    cursor.close()
    connection.close()


def update_task(new_title, new_time, id_):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f"UPDATE {TABLE_NAME} "
        "SET task_title = ?, task_time = ? "
        "WHERE id = ?",
        (new_title, new_time, id_)
    )

    connection.commit()

    cursor.close()
    connection.close()


def remove_task(task_id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f"DELETE FROM {TABLE_NAME} WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()


def get_all():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f"SELECT * FROM {TABLE_NAME}"
    )

    task_list = cursor.fetchall()

    cursor.close()
    connection.close()

    return task_list
