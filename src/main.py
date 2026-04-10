import argparse

from CRUD.add_tasks import add_tasks
from CRUD.delate_tasks import delete_task
from CRUD.read_tasks import read_task
from CRUD.update_tasks import update_task


def main():
    parser = argparse.ArgumentParser(
        prog="task-tracker-cli", description="A simple CLI for tracking tasks"
    )
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="The task to add")

    update_parser = subparsers.add_parser("update", help="Update task")
    update_parser.add_argument("id", type=int, help="Id to update")
    update_parser.add_argument("description", type=str, help="Description to update")

    delete_parser = subparsers.add_parser("delete", help="Delete task")
    delete_parser.add_argument("id", type=int, help="Id to delete")

    read_parser = subparsers.add_parser("list", help="List all tasks")
    read_parser.add_argument(
        "status",
        nargs="?",
        choices=["todo", "done", "in-progress"],
        help="Filter by status",
    )

    args = parser.parse_args()

    match args.command:
        case "add":
            add_tasks(args.description)
        case "update":
            update_task(args.id, args.description)
        case "delete":
            delete_task(args.id)
        case "list":
            read_task(args.status)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
