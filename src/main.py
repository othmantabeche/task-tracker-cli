import argparse

from add_tasks import add_tasks


def main():
    parser = argparse.ArgumentParser(
        prog="task-tracker-cli", description="A simple CLI for tracking tasks"
    )
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="The task to add")

    args = parser.parse_args()

    match args.command:
        case "add":
            add_tasks(args.task)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
