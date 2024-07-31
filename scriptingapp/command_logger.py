from database import init_db, log_command_to_db
from logger import log_command_to_file
from command import delete_log_files, rename_log_file

def log_command_to_db_wrapper(command):
    """Log a command to both the database and the text file."""
    log_command_to_file(command)  # Log to text file
    log_command_to_db(command)    # Log to database

def execute_command(command):
    """Execute a command and log it."""
    parts = command.split()
    if parts[0] == "--del":
        delete_log_files()
    elif parts[0] == "--rename" and len(parts) == 3:
        old_name = parts[1]
        new_name = parts[2]
        rename_log_file(old_name, new_name)
    else:
        log_command_to_db_wrapper(command)
        # Here you could also execute the command if needed (e.g., using subprocess)

def main():
    """Main function to initialize the database and handle user input."""
    init_db()  # Initialize the database
    print("Welcome to the Command Logger Application!")
    print("Type your commands below. Type 'exit' or 'quit' to stop.")
    print("Available commands:")
    print("--del: Delete all log files")
    print("--rename <old_name> <new_name>: Rename a log file")

    while True:
        try:
            command = input("Enter command: ")  # Read user input
            if command.lower() in ["exit", "quit"]:  # Check if the user wants to quit
                break
            execute_command(command)  # Execute the command
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
