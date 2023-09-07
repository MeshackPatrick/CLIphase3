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
@click.argument("username")
@click.argument("password")
def register(username, password):
    """Register a new user."""
    create_user(username, password)


@cli.command()
@click.argument("username")
@click.argument("password")
def login(username, password):
    """Log in as a registered user."""
    user = authenticate_user(username, password)
    if user:
        click.echo(f"Logged in as {user.username}.")
    else:
        click.echo("Login failed. Invalid credentials.")


@cli.command()
@click.argument("description")
@click.argument("due_date")
@click.option("--username", default=None, help="Assign the task to a specific user (if logged in).")
def add(description, due_date, username):
    """Add a new task with a due date."""
    add_task(description, due_date, username)


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
