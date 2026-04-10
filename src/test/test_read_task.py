import io
import json
import os
import unittest
from unittest.mock import patch

from CRUD.read_tasks import read_task

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks_test.json")


class TestReadTasks(unittest.TestCase):
    def setUp(self):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)

    def test_read_tasks_empty(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            read_task(file_path=FILE_PATH)
            self.assertIn("No tasks found.", mock_stdout.getvalue())

    def test_read_all_tasks(self):
        with open(FILE_PATH, "w") as f:
            json.dump(
                [
                    {"id": 1, "description": "Task 1", "status": "todo"},
                    {"id": 2, "description": "Task 2", "status": "done"},
                ],
                f,
            )

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            read_task(file_path=FILE_PATH)
            output = mock_stdout.getvalue()
            self.assertIn("'description': 'Task 1'", output)
            self.assertIn("'description': 'Task 2'", output)

    def test_read_tasks_by_status(self):
        with open(FILE_PATH, "w") as f:
            json.dump(
                [
                    {"id": 1, "description": "Task 1", "status": "todo"},
                    {"id": 2, "description": "Task 2", "status": "done"},
                    {"id": 3, "description": "Task 3", "status": "in-progress"},
                ],
                f,
            )

        # Test reading 'todo'
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            read_task(status="todo", file_path=FILE_PATH)
            output = mock_stdout.getvalue()
            self.assertIn("'description': 'Task 1'", output)
            self.assertNotIn("'description': 'Task 2'", output)
            self.assertNotIn("'description': 'Task 3'", output)

        # Test reading 'done'
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            read_task(status="done", file_path=FILE_PATH)
            output = mock_stdout.getvalue()
            self.assertNotIn("'description': 'Task 1'", output)
            self.assertIn("'description': 'Task 2'", output)
            self.assertNotIn("'description': 'Task 3'", output)

    def tearDown(self):
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
