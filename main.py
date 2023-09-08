import click
from db import create_database, create_user, authenticate_user, add_task, list_tasks, remind_tasks


@click.group()
def cli():
    """To-Do List with Reminders CLI."""
    pass


@cli.command()
def initdb():
    """Initialize the database."""
    create_database()


@cli.command()
def register():
    """Register a new user."""
    username = click.prompt("Enter your username")
    password = click.prompt("Enter your password", hide_input=True, confirmation_prompt=True)

    create_user(username, password)


@cli.command()
def login():
    """Log in as a registered user."""
    username = click.prompt("Enter your username")
    password = click.prompt("Enter your password", hide_input=True)

    user = authenticate_user(username, password)
    if user:
        click.echo(f"Logged in as {user.username}.")
        add_task_description = click.prompt("Enter the task description")
        due_date = click.prompt("Enter the due date (YYYY-MM-DD)")
        add_task(add_task_description, due_date, username)
    else:
        click.echo("Login failed. Invalid credentials.")


@cli.command()
@click.option("--username", default=None, help="List tasks for a specific user (if logged in).")
def list(username):
    """List all tasks."""
    list_tasks(username)


@cli.command()
def remind():
    """Remind about upcoming tasks."""
    remind_tasks()


if __name__ == "__main__":
    cli()
