# import basemodel to create the instance model type for request bodies
from pydantic import BaseModel

class Task(BaseModel):
    task: str
    status: str = None

class Todo(BaseModel):
    id: int
    task: Task

class TodoTask(BaseModel):
    task: str