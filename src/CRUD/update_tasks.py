import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")


def update_task(id: int, description: str, file_path=FILE_PATH) -> None:
    if not id or not description:
        print("ID and description are required to update a task.")
        return

    if not os.path.exists(file_path):
        print("No tasks found to update.")
        return

    with open(file_path, "r") as f:
        tasks = json.load(f)

    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            with open(file_path, "w") as f:
                json.dump(tasks, f, indent=4)
            print(f"Task with ID {id} updated successfully.")
            return
