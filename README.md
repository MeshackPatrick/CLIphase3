# To-Do List with Reminders
A simple To-Do List application with reminders implemented as a command-line interface (CLI) using Python and SQLAlchemy.

# Features
. User-friendly command-line interface (CLI).
. Create, edit, and delete tasks.
. Assign due dates to tasks.
. List all tasks or filter by status and due date.
. Set reminders for tasks with due dates.
. Secure user registration and authentication.
. Data storage in an SQLite database.

# Getting Started

# Prerequisites
Before you begin, ensure you have the following prerequisites:

1. Python 3.x installed on your system.
2. pip package manager installed.

# Installation
1. Clone the Repository:


    git clone https://github.com/misheckPatrick/CLIphase3

2 .Navigate to the Project Directory:

    cd todo-list

Install Dependencies:

    pip install -r requirements.txt

This will install the required Python packages.

4 .Initialize the Database:

    python main.py initdb

# Usage
To use the To-Do List with reminders, you can run the following command from the project directory:

    python main.py <command> [options]
# Commands
1. register <username> <password>: Register a new user.
2. login <username> <password>: Log in as a registered user.
3. logout: Log out the current user.
4. add <description> <due_date>: Add a new task with a due date.
5. edit <task_id> <description> <due_date>: Edit an existing task.
6. delete <task_id>: Delete a task.
7. list [--all] [--completed] [--pending] [--due_date] [--username <username>]: List tasks based on filters.
8. remind: Display reminders for tasks with due dates.

# Customization
You can customize and extend the project to suit your needs. Consider the following:
    .Enhancing the CLI with more features.
    .Implementing additional task attributes (e.g., priority, tags).
    .Adding support for different database systems.
    .Improving security features (e.g., password hashing).

# Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Create a pull request to merge your changes into the main branch.

# License
This project is licensed under the MIT License.





