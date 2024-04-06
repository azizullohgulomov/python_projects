# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")


# Function to remove a task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found.")


# Function to display all tasks
def display_tasks():
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

add_task("Buy groceries")
add_task("Complete homework")
add_task("Call mom")
display_tasks()
remove_task("Buy groceries")
display_tasks()