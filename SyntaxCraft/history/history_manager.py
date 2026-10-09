"""
SyntaxCraft - History Manager
Module: history.history_manager

Lightweight local storage for generated Python solutions using Python's built-in sqlite3.
No external database server is used.
"""

import os
import sqlite3
from datetime import datetime
from typing import List, Dict, Any

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "history.db")


def get_db_connection():
    """Establish a connection to the local SQLite database."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Ensure the history table is created."""
    conn = get_db_connection()
    try:
        with conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prompt TEXT NOT NULL,
                    difficulty TEXT NOT NULL,
                    task TEXT NOT NULL,
                    code TEXT NOT NULL,
                    timestamp TEXT NOT NULL
                )
                """
            )
    finally:
        conn.close()


def add_history(prompt: str, difficulty: str, task: str, code: str) -> int:
    """Insert a new code generation record into history."""
    init_db()
    conn = get_db_connection()
    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with conn:
            cursor = conn.execute(
                """
                INSERT INTO history (prompt, difficulty, task, code, timestamp)
                VALUES (?, ?, ?, ?, ?)
                """,
                (prompt.strip(), difficulty.strip(), task.strip(), code.strip(), timestamp_str)
            )
            return cursor.lastrowid
    finally:
        conn.close()


def get_history(limit: int = 50) -> List[Dict[str, Any]]:
    """Retrieve history records ordered by newest first."""
    init_db()
    conn = get_db_connection()
    try:
        cursor = conn.execute(
            """
            SELECT id, prompt, difficulty, task, code, timestamp
            FROM history
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )
        rows = cursor.fetchall()
        return [
            {
                "id": row["id"],
                "prompt": row["prompt"],
                "difficulty": row["difficulty"],
                "task": row["task"],
                "code": row["code"],
                "timestamp": row["timestamp"]
            }
            for row in rows
        ]
    finally:
        conn.close()


def clear_history() -> bool:
    """Clear all records from history."""
    init_db()
    conn = get_db_connection()
    try:
        with conn:
            conn.execute("DELETE FROM history")
        return True
    finally:
        conn.close()


# Initialize database upon import
init_db()
