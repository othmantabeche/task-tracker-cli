import json
import os
import unittest

from add_tasks import add_tasks

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks_test.json")


class TestAddTasks(unittest.TestCase):
    def setUp(self):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)

    def test_add_task(self):
        # Test adding a valid task
        add_tasks("Test task 1", FILE_PATH)
        with open(FILE_PATH, "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test task 1")

    def test_add_task_empty(self):
        # Test adding an empty task
        add_tasks("", FILE_PATH)
        with open(FILE_PATH, "r") as f:
            tasks = json.load(f)
        self.assertEqual(len(tasks), 0)  # No new task should be added
