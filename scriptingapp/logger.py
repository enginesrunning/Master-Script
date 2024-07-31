import datetime
import sqlite3

# Define the log file path
LOG_FILE_PATH = r'C:\Users\uig95551\Desktop\summerpractice\scriptingapp\command_log.txt'

# Define the database path
DB_PATH = r'C:\Users\uig95551\Desktop\summerpractice\scriptingapp\commands.db'

def log_command_to_file(command):
    """Log a command to a text file with a timestamp."""
    try:
        with open(LOG_FILE_PATH, "a") as log_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} - {command}\n")
        print(f"Logged to file: {LOG_FILE_PATH}")  # Debug print
    except Exception as e:
        print(f"Failed to log to file: {e}")

# No longer need this in logger.py to avoid circular import
# def log_command_to_db_wrapper(command):
#    log_command_to_file(command)
#    log_command_to_db(command)
