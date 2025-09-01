# lib/db.py
import sqlite3

# Use a module-level singleton connection & cursor
CONN = sqlite3.connect(":memory:", check_same_thread=False)
CURSOR = CONN.cursor()

def reset_db():
    """Drop and recreate tables for fresh test runs."""
    CURSOR.execute("DROP TABLE IF EXISTS departments")
    CONN.commit()
