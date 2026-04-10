# Task Tracker CLI

A simple, minimalist command-line interface to manage and track your tasks. Tasks are saved locally in a JSON file.

## Features

- Add, update, and delete tasks.
- List all tasks.
- Filter tasks by status (`todo`, `in-progress`, `done`).
- Automatically generates unique IDs and tracks creation/update times.

## Requirements

- Python 3.13+

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. Check the CLI options:
   ```bash
   PYTHONPATH=src python3 src/main.py -h
   ```

*(Optional: If you use an alias or shell script wrapper, you can replace `PYTHONPATH=src python3 src/main.py` with `task-cli`)*

## Usage

**Add a new task**
```bash
PYTHONPATH=src python3 src/main.py add "Buy groceries"
```

**Update an existing task**
```bash
PYTHONPATH=src python3 src/main.py update 1 "Buy groceries and milk"
```

**Delete a task**
```bash
PYTHONPATH=src python3 src/main.py delete 1
```

**List all tasks**
```bash
PYTHONPATH=src python3 src/main.py list
```

**List tasks by status**
```bash
PYTHONPATH=src python3 src/main.py list todo
PYTHONPATH=src python3 src/main.py list in-progress
PYTHONPATH=src python3 src/main.py list done
```

## Testing

To run the test suite, simply execute the provided bash script:

```bash
./test.sh
```
