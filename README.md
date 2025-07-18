# To-Do List CLI App

This is a simple command-line To-Do List application written in Python. It allows users to add, delete, and mark tasks as completed. All tasks are saved locally in a plain text file for persistent storage.

---

## Features

* Add new tasks
* Delete existing tasks
* Mark tasks as completed
* View all tasks with status (Completed / Not Completed)
* Save and persist tasks in a local file (`tasks.txt`)

---

## Requirements

* Python 3.x

No external libraries are required—only Python's built-in functionality is used.

---

## How It Works

When the script is executed:

1. It attempts to load tasks from `tasks.txt`.
2. If the file doesn't exist, a new one is created.
3. The user is presented with a menu to manage tasks:

   * Show all tasks
   * Add a new task
   * Delete an existing task
   * Mark a task as completed
   * Exit the application

Changes are automatically saved after any modification.

---

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/todo-cli.git
   cd todo-cli
   ```

2. Run the program:

   ```bash
   python todo.py
   ```

3. Use the on-screen menu to interact with your to-do list.

---

## Data Format

Tasks are saved in a `tasks.txt` file using the following format:

```
Task description|yes
Another task|no
```

* `yes` indicates the task is completed.
* `no` indicates it is not yet completed.

---

## Example Output

```
Welcome to your to-do list!

    1. Show Tasks
    2. Add a task
    3. Delete a task
    4. Mark a task as completed
    5. Save and exit

    What's your choice? 2
    Enter the new task: Read a book
    Task added successfully!
```

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributing

Contributions and suggestions are welcome. Feel free to open an issue or submit a pull request.

---
