import sqlite3

def init_db():
    conn = sqlite3.connect("edgewise.db")
    cursor = conn.cursor()

    # Table for motion events
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS motion_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            event_type TEXT NOT NULL,
            message TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized: edgewise.db")

if __name__ == "__main__":
    init_db()
