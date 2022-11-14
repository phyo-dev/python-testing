# import fastapi module
from fastapi import FastAPI

from todo import todo_router

# create instance object of fastapi
app = FastAPI()

@app.get('/')
def index() -> dict:
    return {"msg":"Hello World"}

# include todo_router to include mutli routes
app.include_router(todo_router)