class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task: {self.name}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                print(f"Task {index}:")
                print(task)
                print()
        else:
            print("No tasks available.")

    def mark_task_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority: ")
            task = Task(name, due_date, priority)
            task_manager.add_task(task)
            print("Task added successfully.")
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            task_manager.mark_task_completed(index)
        elif choice == '4':
            index = int(input("Enter task index to remove: "))
            task_manager.remove_task(index)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
