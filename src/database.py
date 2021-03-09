import sqlite3
from sqlite3 import Error


DB_PATH = "db/stockr.db"


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        print(f"✅ Launched database v{sqlite3.version}")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
