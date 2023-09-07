from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

DATABASE_URI = "sqlite:///todo.db"

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    tasks = relationship("Task", backref="user", lazy=True)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    due_dates = relationship("DueDate", backref="task", lazy=True)


class DueDate(Base):
    __tablename__ = "due_dates"

    id = Column(Integer, primary_key=True)
    due_date = Column(Date, nullable=False, default=datetime.now().date())
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)