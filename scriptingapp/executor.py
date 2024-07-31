import subprocess
from logger import log_command_to_db_wrapper

def execute_command(command):
    try:
        log_command_to_db_wrapper(command)
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f"Error executing command: {e}")

