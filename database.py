import sqlite3
from datetime import datetime

conn = sqlite3.connect("prayer.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prayer_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        category TEXT,
        message TEXT,
        approved INTEGER DEFAULT 0,
        prayer_count INTEGER DEFAULT 0,
        created_at TEXT
    )
    """)
    conn.commit()

def insert_request(user_id, category, message):
    cursor.execute("""
        INSERT INTO prayer_requests (user_id, category, message, created_at)
        VALUES (?, ?, ?, ?)
    """, (user_id, category, message, datetime.now().isoformat()))
    conn.commit()
    return cursor.lastrowid

def approve_request(prayer_id):
    cursor.execute("UPDATE prayer_requests SET approved=1 WHERE id=?", (prayer_id,))
    conn.commit()

def get_request(prayer_id):
    cursor.execute("SELECT * FROM prayer_requests WHERE id=?", (prayer_id,))
    return cursor.fetchone()

def get_random_request():
    cursor.execute("SELECT * FROM prayer_requests WHERE approved=1 ORDER BY RANDOM() LIMIT 1")
    return cursor.fetchone()

def increment_prayer(prayer_id):
    cursor.execute("""
        UPDATE prayer_requests
        SET prayer_count = prayer_count + 1
        WHERE id=?
    """, (prayer_id,))
    conn.commit()

    cursor.execute("SELECT prayer_count FROM prayer_requests WHERE id=?", (prayer_id,))
    return cursor.fetchone()[0]