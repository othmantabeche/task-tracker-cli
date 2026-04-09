import json
import os

from utils.random_id import random_id

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")


def add_tasks(task: str, file_path=FILE_PATH) -> None:

    if not task:
        return

    id = random_id()
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)

    with open(file_path, "r") as f:
        tasks = json.load(f)

    tasks.append({"id": id, "task": task})

    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=4)
        print(f"Task added successfully (ID: {id})")
