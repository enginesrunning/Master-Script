import sqlite3
import datetime

# Define the database path
DB_PATH = r'C:\Users\uig95551\Desktop\summerpractice\scriptingapp\commands.db'

def init_db():
    """Initialize the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS commands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            command TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_command_to_db(command):
    """Log a command to the database with a timestamp."""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute('''
            INSERT INTO commands (timestamp, command) VALUES (?, ?)
        ''', (timestamp, command))
        conn.commit()
        conn.close()
        print("Logged to database")
    except Exception as e:
        print(f"Failed to log to database: {e}")
