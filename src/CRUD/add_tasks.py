import json
import os

from Task import Task
from utils.random_id import random_id

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")


def add_tasks(description: str, file_path=FILE_PATH) -> None:

    if not description:
        return

    id = random_id()
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)

    with open(file_path, "r") as f:
        tasks = json.load(f)

    task = Task(id=id, description=description)
    tasks.append(task.to_dict())

    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=4)
        print(f"Task added successfully (ID: {id})")
