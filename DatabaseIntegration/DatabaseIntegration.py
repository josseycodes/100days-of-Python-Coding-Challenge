import sqlite3

# Connect to the database (creates a new database if not exists)
conn = sqlite3.connect("todo_list.db")

# Create a table to store todo items
conn.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY,
        task TEXT NOT NULL,
        status TEXT NOT NULL
    )
""")

# Function to add a new todo item to the database
def add_todo_item(task, status):
    conn.execute("INSERT INTO todos (task, status) VALUES (?, ?)", (task, status))
    conn.commit()

# Function to retrieve all todo items from the database
def get_todo_items():
    cursor = conn.execute("SELECT * FROM todos")
    return cursor.fetchall()

# Function to update a todo item's status in the database
def update_todo_status(todo_id, new_status):
    conn.execute("UPDATE todos SET status=? WHERE id=?", (new_status, todo_id))
    conn.commit()

# Function to delete a todo item from the database
def delete_todo_item(todo_id):
    conn.execute("DELETE FROM todos WHERE id=?", (todo_id,))
    conn.commit()

# Example usage
if __name__ == "__main__":
    # Add a new todo item
    add_todo_item("Buy groceries", "Incomplete")

    # Retrieve all todo items
    todos = get_todo_items()
    print("Todo List:")
    for todo in todos:
        print(f"{todo[0]}. {todo[1]} - Status: {todo[2]}")

    # Update the status of a todo item
    todo_id = 1
    new_status = "Complete"
    update_todo_status(todo_id, new_status)

    # Delete a todo item
    todo_id = 1
    delete_todo_item(todo_id)

    # Retrieve updated todo list
    todos = get_todo_items()
    print("Updated Todo List:")
    for todo in todos:
        print(f"{todo[0]}. {todo[1]} - Status: {todo[2]}")

    # Close the database connection
    conn.close()

