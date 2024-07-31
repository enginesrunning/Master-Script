import os
import glob

LOG_DIR = r'C:\Users\uig95551\Desktop\summerpractice\scriptingapp\logs'

def delete_log_files():import os
import glob

LOG_DIR = r'C:\Users\uig95551\Desktop\summerpractice\scriptingapp\logs'

def delete_log_files():
    """Delete all log files in the specified log directory."""
    if not os.path.exists(LOG_DIR):
        print(f"Log directory {LOG_DIR} does not exist.")
        return

    log_files = glob.glob(os.path.join(LOG_DIR, "*.txt"))
    if not log_files:
        print("No log files found to delete.")
        return

    for log_file in log_files:
        try:
            os.remove(log_file)
            print(f"Deleted log file: {log_file}")
        except Exception as e:
            print(f"Failed to delete {log_file}: {e}")

def rename_log_file(old_name, new_name):
    """Rename a log file in the specified log directory."""
    old_file_path = os.path.join(LOG_DIR, old_name)
    new_file_path = os.path.join(LOG_DIR, new_name)

    if not os.path.exists(old_file_path):
        print(f"Log file {old_file_path} does not exist.")
        return

    try:
        os.rename(old_file_path, new_file_path)
        print(f"Renamed log file from {old_file_path} to {new_file_path}")
    except Exception as e:
        print(f"Failed to rename log file: {e}")

    """Delete all log files in the specified log directory."""
    if not os.path.exists(LOG_DIR):
        print(f"Log directory {LOG_DIR} does not exist.")
        return

    log_files = glob.glob(os.path.join(LOG_DIR, "*.txt"))
    if not log_files:
        print("No log files found to delete.")
        return

    for log_file in log_files:
        try:
            os.remove(log_file)
            print(f"Deleted log file: {log_file}")
        except Exception as e:
            print(f"Failed to delete {log_file}: {e}")

def rename_log_file(old_name, new_name):
    """Rename a log file in the specified log directory."""
    old_file_path = os.path.join(LOG_DIR, old_name)
    new_file_path = os.path.join(LOG_DIR, new_name)

    if not os.path.exists(old_file_path):
        print(f"Log file {old_file_path} does not exist.")
        return

    try:
        os.rename(old_file_path, new_file_path)
        print(f"Renamed log file from {old_file_path} to {new_file_path}")
    except Exception as e:
        print(f"Failed to rename log file: {e}")
