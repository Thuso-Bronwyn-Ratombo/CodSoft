import json

import os

def center_text(text):
    # Get the width of the terminal
    terminal_width = os.get_terminal_size().columns
    
    # Calculate the length of the text
    text_length = len(text)
    
    # Calculate padding
    padding = (terminal_width - text_length) // 2
    
    # Return the centered text
    return ' ' * padding + text

# Example Usage
if __name__ == "__main__":
    print(center_text("Welcome to the To-Do List Application"))
    print(center_text("Select an option below:"))


class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks = json.load(file)
                self.tasks = [Task(**task) for task in tasks]
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty list.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == '6':
            filename = input("Enter filename to load tasks: ")
            todo_list.load_tasks(filename)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
