import json
import os
import unittest

from CRUD.delate_tasks import delete_task

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks_test.json")


class TestDeleteTasks(unittest.TestCase):
    def setUp(self):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)

    def test_delete_task(self):
        # Add a task to delete
        with open(FILE_PATH, "w") as f:
            json.dump([{"id": 1, "description": "Task to delete"}], f)

        # Delete the task
        delete_task(1, FILE_PATH)

        # Verify the task was deleted
        with open(FILE_PATH, "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 0)  # Task should be deleted

    def test_delete_nonexistent_task(self):
        # Try to delete a task that doesn't exist
        delete_task(999, FILE_PATH)

        # Verify no tasks were deleted
        with open(FILE_PATH, "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 0)  # No tasks should be deleted

    def tearDown(self):
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
