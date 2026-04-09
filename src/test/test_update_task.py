import json
import os
import unittest

from CRUD.update_tasks import update_task

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks_test.json")


class TestUpdateTasks(unittest.TestCase):
    def setUp(self):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)

    def test_update_task(self):
        # Add a task to update
        with open(FILE_PATH, "w") as f:
            json.dump([{"id": 1, "description": "Old description"}], f)

        # Update the task
        update_task(1, "New description", FILE_PATH)

        # Verify the task was updated
        with open(FILE_PATH, "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "New description")

    def test_update_nonexistent_task(self):
        # Try to update a task that doesn't exist
        update_task(999, "Should not update", FILE_PATH)

        # Verify no tasks were updated
        with open(FILE_PATH, "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 0)  # No tasks should be updated
