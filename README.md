# Daily Task

A simple terminal-based daily task manager built with Python and SQLite.

The project was created to practice Python fundamentals, object-oriented programming, database persistence, input validation and project organization.

## Features

- Add daily tasks
- List tasks
- Mark and unmark tasks as completed
- Edit tasks
- Remove tasks
- Store tasks locally with SQLite
- Organize tasks by time

## Technologies

- Python
- SQLite
- Rich

## Project Structure

```text
daily-task/
├── main.py
├── tasks.py
├── database.py
├── input_validation.py
├── menus.py
└── README.md
```

## Running the project

Clone the repository:

```bash
git clone https://github.com/your-username/daily-task.git
```

Enter the project directory:

```bash
cd daily-task
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install rich
```

Run the application:

```bash
python main.py
```

## Purpose

This project is part of my software development studies and is being used to practice building a complete application from scratch, including application logic, persistence and code organization.

## Future Improvements

- Refactor the terminal interface using Rich
- Improve menu organization
- Automatically reset completed tasks each day
- Add better task visualization
- Add tests
