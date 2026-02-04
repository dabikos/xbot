# TodoList Application

A simple, command-line todo list application written in Python. This application allows you to manage your tasks with basic operations like adding, removing, completing, and listing tasks.

## Features

- ✅ Add tasks with titles and optional descriptions
- ✅ Mark tasks as complete/incomplete
- ✅ List all tasks, or filter by completed/pending status
- ✅ Remove individual tasks
- ✅ Clear all completed tasks at once
- ✅ Persistent storage in JSON format
- ✅ Simple command-line interface

## Installation

No additional dependencies are required beyond Python 3.6+. The application uses only Python standard library modules.

```bash
# Clone or download the repository
git clone <repository-url>
cd xbot

# The todolist.py file is ready to use
python todolist.py
```

## Usage

### Basic Commands

```bash
# Display help
python todolist.py

# Add a new task
python todolist.py add "Task title" "Optional description"

# List all tasks
python todolist.py list

# List only completed tasks
python todolist.py list done

# List only pending tasks
python todolist.py list pending

# Mark a task as complete
python todolist.py complete <task_id>

# Mark a task as incomplete
python todolist.py incomplete <task_id>

# Remove a specific task
python todolist.py remove <task_id>

# Clear all completed tasks
python todolist.py clear
```

### Examples

```bash
# Add some tasks
python todolist.py add "Buy groceries" "Get milk, eggs, and bread"
python todolist.py add "Write report"
python todolist.py add "Call dentist"

# List all tasks
python todolist.py list
# Output:
# All tasks:
#   [ ] 1. Buy groceries
#   [ ] 2. Write report
#   [ ] 3. Call dentist

# Complete a task
python todolist.py complete 1

# List completed tasks
python todolist.py list done
# Output:
# Completed tasks:
#   [✓] 1. Buy groceries

# List pending tasks
python todolist.py list pending
# Output:
# Pending tasks:
#   [ ] 2. Write report
#   [ ] 3. Call dentist

# Remove a task
python todolist.py remove 2

# Clear all completed tasks
python todolist.py clear
```

## Data Persistence

Tasks are automatically saved to `todos.json` in the current directory after each operation. The data persists between sessions, so you can close the application and your tasks will still be there when you come back.

## Running Tests

The application includes comprehensive unit tests. To run them:

```bash
# Run all tests
python -m unittest test_todolist -v

# Run specific test class
python -m unittest test_todolist.TestTask -v
python -m unittest test_todolist.TestTodoList -v
```

All tests should pass successfully:
```
Ran 29 tests in 0.004s

OK
```

## API Usage

You can also use the TodoList class directly in your Python code:

```python
from todolist import TodoList, Task

# Create a new todo list
todo = TodoList()

# Add tasks
task1 = todo.add_task("Task 1", "Description")
task2 = todo.add_task("Task 2")

# Mark task as complete
todo.mark_complete(task1.id)

# Get all tasks
all_tasks = todo.list_all()
completed_tasks = todo.list_completed()
pending_tasks = todo.list_incomplete()

# Save to file
todo.save_to_file('my_todos.json')

# Load from file
todo.load_from_file('my_todos.json')
```

## Architecture

The application consists of two main classes:

- **Task**: Represents a single task with properties like title, description, completion status, and timestamps
- **TodoList**: Manages a collection of tasks with methods for CRUD operations and filtering

### Task Class

- `title`: The task title (required)
- `description`: Optional task description
- `id`: Unique task identifier
- `completed`: Boolean completion status
- `created_at`: ISO timestamp of creation
- `completed_at`: ISO timestamp of completion (if applicable)

### TodoList Class

Methods:
- `add_task(title, description)`: Add a new task
- `remove_task(task_id)`: Remove a task by ID
- `get_task(task_id)`: Get a task by ID
- `mark_complete(task_id)`: Mark task as complete
- `mark_incomplete(task_id)`: Mark task as incomplete
- `list_all()`: Get all tasks
- `list_completed()`: Get completed tasks only
- `list_incomplete()`: Get incomplete tasks only
- `clear_completed()`: Remove all completed tasks
- `save_to_file(filename)`: Save to JSON file
- `load_from_file(filename)`: Load from JSON file

## License

This project is open source and available for use.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
