# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to mark a task as completed
def complete_task():
    if len(tasks) == 0:
        print("No tasks in the list!")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

        task_index = int(input("Enter the task number to mark as completed: "))
        if task_index < 1 or task_index > len(tasks):
            print("Invalid task number!")
        else:
            completed_task = tasks.pop(task_index - 1)
            print(f"Task '{completed_task}' marked as completed!")

# Function to remove a task from the list
def remove_task():
    if len(tasks) == 0:
        print("No tasks in the list!")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

        task_index = int(input("Enter the task number to remove: "))
        if task_index < 1 or task_index > len(tasks):
            print("Invalid task number!")
        else:
            removed_task = tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed from the list!")

# Main program loop
while True:
    print("\n---- To-Do List Application ----")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        complete_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 4.")

