import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")


def read_task(status=None, file_path=FILE_PATH) -> None:
    if not os.path.exists(file_path):
        print("No tasks found.")
        return

    with open(file_path, "r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            print("No tasks found.")
            return

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        if status:
            if task.get("status") == status:
                print(task)
        else:
            print(task)
