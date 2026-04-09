import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")


def delete_task(id: int, file_path=FILE_PATH) -> None:
    if not id:
        print("ID is required to delete a task.")
        return

    if not os.path.exists(file_path):
        print("No tasks found to delete.")
        return

    with open(file_path, "r") as f:
        tasks = json.load(f)

    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            with open(file_path, "w") as f:
                json.dump(tasks, f, indent=4)
            print(f"Task with ID {id} deleted successfully.")
            return
    print(f"No task found with ID {id}.")
