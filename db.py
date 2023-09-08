from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Task, DueDate
from datetime import datetime, timedelta
DATABASE_URI = "sqlite:///todo.db"

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


def create_database():
    Base.metadata.create_all(engine)


def create_user(username, password):
    user = User(username=username, password=password)
    session.add(user)
    session.commit()


def authenticate_user(username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    return user


def add_task(description, due_date, username=None):
    if username:
        user = session.query(User).filter_by(username=username).first()
    else:
        user = None

    task = Task(description=description, user=user)
    session.add(task)
    session.commit()

    due_date_obj = DueDate(due_date=datetime.strptime(due_date, "%Y-%m-%d"), task=task)
    session.add(due_date_obj)
    session.commit()


def list_tasks(username=None):
    if username:
        user = session.query(User).filter_by(username=username).first()
        tasks = user.tasks if user else []
    else:
        tasks = session.query(Task).all()

    for task in tasks:
        due_date = task.due_dates[0].due_date.strftime("%Y-%m-%d")
        print(f"Task: {task.description} (Due Date: {due_date})")


def remind_tasks():
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    tasks = session.query(DueDate).filter(DueDate.due_date == tomorrow).all()

    if tasks:
        print("Upcoming tasks for tomorrow:")
        for task in tasks:
            print(f"Task: {task.task.description}")
