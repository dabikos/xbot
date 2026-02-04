"""
A simple todolist application.

This module provides functionality to manage a todo list with basic operations:
- Add tasks
- Remove tasks
- Mark tasks as complete
- List all tasks
- Filter tasks by status
"""

import json
from datetime import datetime
from typing import List, Dict, Optional


class Task:
    """Represents a single task in the todo list."""
    
    def __init__(self, title: str, description: str = "", task_id: Optional[int] = None):
        """
        Initialize a new task.
        
        Args:
            title: The title of the task
            description: Optional description of the task
            task_id: Optional task ID (auto-generated if not provided)
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.completed_at = None
    
    def mark_complete(self):
        """Mark the task as complete."""
        self.completed = True
        self.completed_at = datetime.now().isoformat()
    
    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False
        self.completed_at = None
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary representation."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create a task from dictionary representation."""
        task = cls(data['title'], data.get('description', ''), data.get('id'))
        task.completed = data.get('completed', False)
        task.created_at = data.get('created_at', datetime.now().isoformat())
        task.completed_at = data.get('completed_at')
        return task
    
    def __str__(self) -> str:
        """String representation of the task."""
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}. {self.title}"
    
    def __repr__(self) -> str:
        """Representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"


class TodoList:
    """Manages a collection of tasks."""
    
    def __init__(self):
        """Initialize an empty todo list."""
        self.tasks: List[Task] = []
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the list.
        
        Args:
            title: The title of the task
            description: Optional description of the task
            
        Returns:
            The created task
        """
        task = Task(title, description, self.next_id)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def remove_task(self, task_id: int) -> bool:
        """
        Remove a task from the list.
        
        Args:
            task_id: The ID of the task to remove
            
        Returns:
            True if task was removed, False if not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by ID.
        
        Args:
            task_id: The ID of the task to get
            
        Returns:
            The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.
        
        Args:
            task_id: The ID of the task to mark complete
            
        Returns:
            True if task was marked complete, False if not found
        """
        task = self.get_task(task_id)
        if task:
            task.mark_complete()
            return True
        return False
    
    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.
        
        Args:
            task_id: The ID of the task to mark incomplete
            
        Returns:
            True if task was marked incomplete, False if not found
        """
        task = self.get_task(task_id)
        if task:
            task.mark_incomplete()
            return True
        return False
    
    def list_all(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            List of all tasks
        """
        return self.tasks.copy()
    
    def list_completed(self) -> List[Task]:
        """
        Get all completed tasks.
        
        Returns:
            List of completed tasks
        """
        return [task for task in self.tasks if task.completed]
    
    def list_incomplete(self) -> List[Task]:
        """
        Get all incomplete tasks.
        
        Returns:
            List of incomplete tasks
        """
        return [task for task in self.tasks if not task.completed]
    
    def clear_completed(self) -> int:
        """
        Remove all completed tasks.
        
        Returns:
            Number of tasks removed
        """
        completed = self.list_completed()
        count = len(completed)
        self.tasks = [task for task in self.tasks if not task.completed]
        return count
    
    def save_to_file(self, filename: str):
        """
        Save the todo list to a JSON file.
        
        Args:
            filename: Path to the file to save to
        """
        data = {
            'next_id': self.next_id,
            'tasks': [task.to_dict() for task in self.tasks]
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def load_from_file(self, filename: str):
        """
        Load the todo list from a JSON file.
        
        Args:
            filename: Path to the file to load from
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.next_id = data.get('next_id', 1)
            self.tasks = [Task.from_dict(task_data) for task_data in data.get('tasks', [])]
        except FileNotFoundError:
            # File doesn't exist yet, start with empty list
            pass
    
    def __len__(self) -> int:
        """Return the number of tasks in the list."""
        return len(self.tasks)
    
    def __str__(self) -> str:
        """String representation of the todo list."""
        if not self.tasks:
            return "Todo list is empty"
        return "\n".join(str(task) for task in self.tasks)


def main():
    """Main function to run the todo list application."""
    import sys
    
    todo = TodoList()
    todo.load_from_file('todos.json')
    
    if len(sys.argv) < 2:
        print("Usage: python todolist.py <command> [arguments]")
        print("\nCommands:")
        print("  add <title> [description]  - Add a new task")
        print("  list [all|done|pending]    - List tasks")
        print("  complete <id>              - Mark task as complete")
        print("  incomplete <id>            - Mark task as incomplete")
        print("  remove <id>                - Remove a task")
        print("  clear                      - Remove all completed tasks")
        return
    
    command = sys.argv[1].lower()
    
    try:
        if command == 'add':
            if len(sys.argv) < 3:
                print("Error: Please provide a task title")
                return
            title = sys.argv[2]
            description = ' '.join(sys.argv[3:]) if len(sys.argv) > 3 else ""
            task = todo.add_task(title, description)
            print(f"Added task: {task}")
            
        elif command == 'list':
            filter_type = sys.argv[2].lower() if len(sys.argv) > 2 else 'all'
            if filter_type == 'done':
                tasks = todo.list_completed()
                print("Completed tasks:")
            elif filter_type == 'pending':
                tasks = todo.list_incomplete()
                print("Pending tasks:")
            else:
                tasks = todo.list_all()
                print("All tasks:")
            
            if tasks:
                for task in tasks:
                    print(f"  {task}")
            else:
                print("  No tasks found")
        
        elif command == 'complete':
            if len(sys.argv) < 3:
                print("Error: Please provide a task ID")
                return
            task_id = int(sys.argv[2])
            if todo.mark_complete(task_id):
                print(f"Marked task {task_id} as complete")
            else:
                print(f"Task {task_id} not found")
        
        elif command == 'incomplete':
            if len(sys.argv) < 3:
                print("Error: Please provide a task ID")
                return
            task_id = int(sys.argv[2])
            if todo.mark_incomplete(task_id):
                print(f"Marked task {task_id} as incomplete")
            else:
                print(f"Task {task_id} not found")
        
        elif command == 'remove':
            if len(sys.argv) < 3:
                print("Error: Please provide a task ID")
                return
            task_id = int(sys.argv[2])
            if todo.remove_task(task_id):
                print(f"Removed task {task_id}")
            else:
                print(f"Task {task_id} not found")
        
        elif command == 'clear':
            count = todo.clear_completed()
            print(f"Removed {count} completed task(s)")
        
        else:
            print(f"Unknown command: {command}")
            return
        
        # Save changes
        todo.save_to_file('todos.json')
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
