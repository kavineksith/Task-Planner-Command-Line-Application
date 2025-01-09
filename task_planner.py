import csv
import os
import sys
import re
from datetime import datetime


class BasePlanner:
    TASK_FILE = "tasks.csv"
    FIELD_NAMES = ["id", "title", "description", "priority", "due_date", "category"]

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the CSV file."""
        if os.path.exists(self.TASK_FILE):
            try:
                with open(self.TASK_FILE, "r", newline="") as file:
                    reader = csv.DictReader(file)
                    self.tasks = list(reader)
            except Exception as e:
                self.handle_error(f"Failed to load tasks - {e}")

    def save_tasks(self):
        """Save tasks to the CSV file."""
        try:
            with open(self.TASK_FILE, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.FIELD_NAMES)
                writer.writeheader()
                writer.writerows(self.tasks)
        except Exception as e:
            self.handle_error(f"Failed to save tasks - {e}")

    def handle_error(self, message):
        """Handle errors."""
        print(f"Error: {message}")
        sys.exit(1)


class TaskPlanner(BasePlanner):
    def __init__(self):
        super().__init__()

    def add_task(self, title, description, priority, due_date, category):
        """Add a new task."""
        task_id = self._generate_task_id()
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "category": category
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully.")

    def _generate_task_id(self):
        """Generate a unique task ID."""
        return max(int(task["id"]) for task in self.tasks) + 1 if self.tasks else 1

    def delete_task(self, task_id):
        """Delete a task by ID."""
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if int(task["id"]) != task_id]
        if len(self.tasks) < initial_count:
            self.save_tasks()
            print("Task deleted successfully.")
        else:
            print(f"No task found with ID: {task_id}.")

    def update_task(self, task_id, **kwargs):
        """Update task details."""
        for task in self.tasks:
            if int(task["id"]) == task_id:
                for key, value in kwargs.items():
                    if key in task:
                        task[key] = value
                self.save_tasks()
                print("Task updated successfully.")
                return
        print(f"No task found with ID: {task_id}.")

    def search_tasks(self, task_id):
        """Search task details."""
        for task in self.tasks:
            if int(task["id"]) == task_id:
                print(task)
                return
        print(f"No task found with ID: {task_id}.")

    def list_tasks(self):
        """List all tasks."""
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)

    @staticmethod
    def validate_input(prompt, regex, required=True):
        """Validate user input using regular expressions."""
        while True:
            user_input = input(prompt)
            if not required and not user_input:
                return user_input
            if re.match(regex, user_input):
                return user_input
            else:
                print("Invalid input. Please try again.")

    @staticmethod
    def validate_date(date_text):
        """Validate date format (YYYY-MM-DD)."""
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def handle_user_choice(self, choice):
        """Handle user menu choice."""
        if choice == "1":
            title = self.validate_input("Enter task title: ", r"^.+$")
            description = self.validate_input("Enter task description: ", r"^.+$")
            priority = self.validate_input("Enter task priority (high/medium/low): ", r"^(high|medium|low)$")
            due_date = self.validate_input("Enter task due date (YYYY-MM-DD): ", r"^\d{4}-\d{2}-\d{2}$")
            while not self.validate_date(due_date):
                print("Invalid date format. Please try again.")
                due_date = self.validate_input("Enter task due date (YYYY-MM-DD): ", r"^\d{4}-\d{2}-\d{2}$")
            category = self.validate_input("Enter task category: ", r"^.+$")
            self.add_task(title, description, priority, due_date, category)

        elif choice == "2":
            task_id = int(self.validate_input("Enter task ID to delete: ", r"^\d+$"))
            self.delete_task(task_id)

        elif choice == "3":
            task_id = int(self.validate_input("Enter task ID to update: ", r"^\d+$"))
            field = self.validate_input("Enter field to update (title/description/priority/due_date/category): ",
                                         r"^(title|description|priority|due_date|category)$")
            value = self.validate_input(f"Enter new value for {field}: ", r"^.+$")
            self.update_task(task_id, **{field: value})

        elif choice == "4":
            print("\nList of Tasks:")
            self.list_tasks()

        elif choice == "5":
            task_id = int(self.validate_input("Enter task ID to search: ", r"^\d+$"))
            self.search_tasks(task_id)

        elif choice == "6":
            print("Exiting Task Manager.")
            sys.exit()

        else:
            print("Invalid choice. Please enter a valid option.")

    def run(self):
        """Run the Task Planner."""
        try:
            while True:
                print("\nTask Planner")
                print("1. Add Task")
                print("2. Delete Task")
                print("3. Update Task")
                print("4. List Tasks")
                print("5. Search Task")
                print("6. Exit")

                choice = self.validate_input("Enter your choice: ", r"^[1-6]$")

                self.handle_user_choice(choice)

        except KeyboardInterrupt:
            print("\nKeyboard Interrupt: Exiting Task Manager.")
        except Exception as e:
            self.handle_error(f"An unexpected error occurred: {e}")


def main():
    task_planner = TaskPlanner()
    task_planner.run()


if __name__ == "__main__":
    main()
