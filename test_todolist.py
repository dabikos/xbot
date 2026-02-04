"""
Tests for the todolist application.
"""

import unittest
import os
import json
import tempfile
from todolist import Task, TodoList


class TestTask(unittest.TestCase):
    """Test cases for the Task class."""
    
    def test_task_creation(self):
        """Test creating a new task."""
        task = Task("Test task", "This is a test", 1)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "This is a test")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.created_at)
        self.assertIsNone(task.completed_at)
    
    def test_task_mark_complete(self):
        """Test marking a task as complete."""
        task = Task("Test task", task_id=1)
        self.assertFalse(task.completed)
        task.mark_complete()
        self.assertTrue(task.completed)
        self.assertIsNotNone(task.completed_at)
    
    def test_task_mark_incomplete(self):
        """Test marking a task as incomplete."""
        task = Task("Test task", task_id=1)
        task.mark_complete()
        self.assertTrue(task.completed)
        task.mark_incomplete()
        self.assertFalse(task.completed)
        self.assertIsNone(task.completed_at)
    
    def test_task_to_dict(self):
        """Test converting task to dictionary."""
        task = Task("Test task", "Description", 1)
        task_dict = task.to_dict()
        self.assertEqual(task_dict['id'], 1)
        self.assertEqual(task_dict['title'], "Test task")
        self.assertEqual(task_dict['description'], "Description")
        self.assertFalse(task_dict['completed'])
        self.assertIn('created_at', task_dict)
    
    def test_task_from_dict(self):
        """Test creating task from dictionary."""
        data = {
            'id': 1,
            'title': "Test task",
            'description': "Description",
            'completed': False,
            'created_at': "2024-01-01T00:00:00",
            'completed_at': None
        }
        task = Task.from_dict(data)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "Description")
        self.assertFalse(task.completed)
    
    def test_task_str(self):
        """Test string representation of task."""
        task = Task("Test task", task_id=1)
        self.assertIn("Test task", str(task))
        self.assertIn("1", str(task))
    
    def test_task_repr(self):
        """Test repr representation of task."""
        task = Task("Test task", task_id=1)
        repr_str = repr(task)
        self.assertIn("Task", repr_str)
        self.assertIn("Test task", repr_str)
        self.assertIn("completed=False", repr_str)


class TestTodoList(unittest.TestCase):
    """Test cases for the TodoList class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.todo = TodoList()
    
    def test_todolist_initialization(self):
        """Test creating a new todo list."""
        self.assertEqual(len(self.todo), 0)
        self.assertEqual(self.todo.next_id, 1)
    
    def test_add_task(self):
        """Test adding a task."""
        task = self.todo.add_task("Test task", "Description")
        self.assertEqual(len(self.todo), 1)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "Description")
    
    def test_add_multiple_tasks(self):
        """Test adding multiple tasks."""
        task1 = self.todo.add_task("Task 1")
        task2 = self.todo.add_task("Task 2")
        task3 = self.todo.add_task("Task 3")
        self.assertEqual(len(self.todo), 3)
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)
    
    def test_get_task(self):
        """Test getting a task by ID."""
        self.todo.add_task("Task 1")
        task2 = self.todo.add_task("Task 2")
        found = self.todo.get_task(2)
        self.assertIsNotNone(found)
        self.assertEqual(found.id, task2.id)
        self.assertEqual(found.title, "Task 2")
    
    def test_get_task_not_found(self):
        """Test getting a non-existent task."""
        self.todo.add_task("Task 1")
        found = self.todo.get_task(999)
        self.assertIsNone(found)
    
    def test_remove_task(self):
        """Test removing a task."""
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")
        self.assertEqual(len(self.todo), 2)
        result = self.todo.remove_task(1)
        self.assertTrue(result)
        self.assertEqual(len(self.todo), 1)
        self.assertIsNone(self.todo.get_task(1))
    
    def test_remove_task_not_found(self):
        """Test removing a non-existent task."""
        self.todo.add_task("Task 1")
        result = self.todo.remove_task(999)
        self.assertFalse(result)
        self.assertEqual(len(self.todo), 1)
    
    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = self.todo.add_task("Task 1")
        result = self.todo.mark_complete(task.id)
        self.assertTrue(result)
        self.assertTrue(task.completed)
    
    def test_mark_complete_not_found(self):
        """Test marking a non-existent task as complete."""
        result = self.todo.mark_complete(999)
        self.assertFalse(result)
    
    def test_mark_incomplete(self):
        """Test marking a task as incomplete."""
        task = self.todo.add_task("Task 1")
        self.todo.mark_complete(task.id)
        self.assertTrue(task.completed)
        result = self.todo.mark_incomplete(task.id)
        self.assertTrue(result)
        self.assertFalse(task.completed)
    
    def test_mark_incomplete_not_found(self):
        """Test marking a non-existent task as incomplete."""
        result = self.todo.mark_incomplete(999)
        self.assertFalse(result)
    
    def test_list_all(self):
        """Test listing all tasks."""
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")
        self.todo.add_task("Task 3")
        all_tasks = self.todo.list_all()
        self.assertEqual(len(all_tasks), 3)
    
    def test_list_completed(self):
        """Test listing completed tasks."""
        task1 = self.todo.add_task("Task 1")
        task2 = self.todo.add_task("Task 2")
        task3 = self.todo.add_task("Task 3")
        
        self.todo.mark_complete(task1.id)
        self.todo.mark_complete(task3.id)
        
        completed = self.todo.list_completed()
        self.assertEqual(len(completed), 2)
        self.assertIn(task1, completed)
        self.assertIn(task3, completed)
        self.assertNotIn(task2, completed)
    
    def test_list_incomplete(self):
        """Test listing incomplete tasks."""
        task1 = self.todo.add_task("Task 1")
        task2 = self.todo.add_task("Task 2")
        task3 = self.todo.add_task("Task 3")
        
        self.todo.mark_complete(task2.id)
        
        incomplete = self.todo.list_incomplete()
        self.assertEqual(len(incomplete), 2)
        self.assertIn(task1, incomplete)
        self.assertIn(task3, incomplete)
        self.assertNotIn(task2, incomplete)
    
    def test_clear_completed(self):
        """Test clearing completed tasks."""
        task1 = self.todo.add_task("Task 1")
        task2 = self.todo.add_task("Task 2")
        task3 = self.todo.add_task("Task 3")
        
        self.todo.mark_complete(task1.id)
        self.todo.mark_complete(task3.id)
        
        count = self.todo.clear_completed()
        self.assertEqual(count, 2)
        self.assertEqual(len(self.todo), 1)
        self.assertIsNone(self.todo.get_task(task1.id))
        self.assertIsNotNone(self.todo.get_task(task2.id))
        self.assertIsNone(self.todo.get_task(task3.id))
    
    def test_save_and_load(self):
        """Test saving and loading from file."""
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_file = f.name
        
        try:
            # Add some tasks and save
            self.todo.add_task("Task 1", "Description 1")
            task2 = self.todo.add_task("Task 2", "Description 2")
            self.todo.add_task("Task 3", "Description 3")
            self.todo.mark_complete(task2.id)
            self.todo.save_to_file(temp_file)
            
            # Create new todo list and load
            new_todo = TodoList()
            new_todo.load_from_file(temp_file)
            
            # Verify
            self.assertEqual(len(new_todo), 3)
            self.assertEqual(new_todo.next_id, 4)
            
            loaded_task2 = new_todo.get_task(2)
            self.assertIsNotNone(loaded_task2)
            self.assertEqual(loaded_task2.title, "Task 2")
            self.assertTrue(loaded_task2.completed)
        finally:
            # Clean up
            if os.path.exists(temp_file):
                os.remove(temp_file)
    
    def test_load_nonexistent_file(self):
        """Test loading from a non-existent file."""
        # Should not raise an error, just start with empty list
        self.todo.load_from_file('nonexistent_file_12345.json')
        self.assertEqual(len(self.todo), 0)
    
    def test_todolist_str_empty(self):
        """Test string representation of empty todo list."""
        result = str(self.todo)
        self.assertIn("empty", result.lower())
    
    def test_todolist_str_with_tasks(self):
        """Test string representation of todo list with tasks."""
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")
        result = str(self.todo)
        self.assertIn("Task 1", result)
        self.assertIn("Task 2", result)
    
    def test_len(self):
        """Test length of todo list."""
        self.assertEqual(len(self.todo), 0)
        self.todo.add_task("Task 1")
        self.assertEqual(len(self.todo), 1)
        self.todo.add_task("Task 2")
        self.assertEqual(len(self.todo), 2)
        self.todo.remove_task(1)
        self.assertEqual(len(self.todo), 1)


class TestTodoListPersistence(unittest.TestCase):
    """Test cases for TodoList persistence."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.filename = self.temp_file.name
    
    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
    
    def test_save_format(self):
        """Test that saved file has correct format."""
        todo = TodoList()
        todo.add_task("Task 1", "Description")
        todo.save_to_file(self.filename)
        
        with open(self.filename, 'r') as f:
            data = json.load(f)
        
        self.assertIn('next_id', data)
        self.assertIn('tasks', data)
        self.assertEqual(len(data['tasks']), 1)
        self.assertEqual(data['tasks'][0]['title'], "Task 1")
    
    def test_persistence_across_instances(self):
        """Test that data persists across different TodoList instances."""
        # First instance
        todo1 = TodoList()
        todo1.add_task("Task 1")
        todo1.add_task("Task 2")
        todo1.save_to_file(self.filename)
        
        # Second instance
        todo2 = TodoList()
        todo2.load_from_file(self.filename)
        todo2.add_task("Task 3")
        todo2.save_to_file(self.filename)
        
        # Third instance
        todo3 = TodoList()
        todo3.load_from_file(self.filename)
        
        self.assertEqual(len(todo3), 3)
        self.assertIsNotNone(todo3.get_task(1))
        self.assertIsNotNone(todo3.get_task(2))
        self.assertIsNotNone(todo3.get_task(3))


if __name__ == '__main__':
    unittest.main()
