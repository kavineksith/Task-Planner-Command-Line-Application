# **Documentation: Task Planner Command-Line Application**

## Overview

The Task Planner is a command-line Python application designed to facilitate task management by providing functionality for adding, deleting, updating, searching, and listing tasks. Tasks are managed through a CSV file, offering a straightforward interface for interaction. This application is intended to help users efficiently organize and track their tasks based on various attributes such as priority, due date, and category.

## Features

- **Task Management**: Add, delete, and update tasks with details such as title, description, priority, due date, and category.
- **Task Search**: Retrieve and display task details based on a unique task ID.
- **Task Listing**: View all tasks in a tabulated format.
- **Input Validation**: Ensure accurate user input through regex validation for various fields including task details and date formats.
- **Error Handling**: Robust error management to handle file operations and unexpected conditions gracefully.

## Dependencies

- **Python 3.x**: The script is compatible with Python 3.x versions. Ensure Python is installed on your system to run the script.
- **Standard Libraries**: Utilizes Python's built-in libraries including:
  - `csv` for reading from and writing to CSV files.
  - `os` for file and directory operations.
  - `sys` for system-specific parameters and functions.
  - `re` for regular expression operations.
  - `datetime` for date manipulations and validations.

No external dependencies or third-party libraries are required.

## Usage

To use the Task Planner, follow these steps:

1. **Clone or Download the Script**: Obtain the script file from the repository or source.
2. **Run the Script**: Execute the script using Python by navigating to the directory containing the script and running the following command:

   ```bash
   python task_planner.py
   ```

3. **Interact with the Command-Line Interface**: Follow the on-screen prompts to manage tasks.

## Interactive Commands

The Task Planner provides the following interactive commands for task management:

1. **Add Task**:
   - **Command**: `1`
   - **Description**: Adds a new task with details such as title, description, priority, due date, and category.
   - **Prompts**: Title, Description, Priority (high/medium/low), Due Date (YYYY-MM-DD), and Category.

2. **Delete Task**:
   - **Command**: `2`
   - **Description**: Deletes an existing task based on the provided task ID.
   - **Prompt**: Task ID to delete.

3. **Update Task**:
   - **Command**: `3`
   - **Description**: Updates details of an existing task identified by its task ID.
   - **Prompts**: Task ID to update, field to update (title/description/priority/due_date/category), and the new value.

4. **List Tasks**:
   - **Command**: `4`
   - **Description**: Lists all tasks currently stored in the system.
   - **Output**: Displays all tasks with their details.

5. **Search Task**:
   - **Command**: `5`
   - **Description**: Searches for a task by its task ID and displays its details.
   - **Prompt**: Task ID to search.

6. **Exit**:
   - **Command**: `6`
   - **Description**: Exits the Task Planner application.

## Special Commands

- **Error Handling**: If an invalid choice is made or an unexpected error occurs, the application will print an error message and exit gracefully.
- **Keyboard Interrupt**: The application handles keyboard interrupts (Ctrl+C) and exits with a message indicating the termination.

## Conclusion

The Task Planner script offers a robust solution for managing tasks via a command-line interface. It combines simplicity with functionality, allowing users to add, delete, update, search, and list tasks efficiently. With built-in error handling and input validation, it ensures a reliable and user-friendly experience. Whether for personal organization or small-scale project management, the Task Planner provides a practical tool for keeping tasks in check.

For further enhancement or customization, users can modify the script to fit specific requirements or integrate additional features.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.
