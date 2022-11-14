# import APIRouter to create todo routes
from fastapi import APIRouter, Path

# import model instance class to accept request
from model import Todo, TodoTask

# create instance object of APIRouter
todo_router = APIRouter()

todo_list = []

@todo_router.get('/todo')
async def get_todo_list() -> dict:
    return {"to_list":todo_list}

@todo_router.post('/todo')
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"msg": "Successfully Added new Todo Task"}

@todo_router.get('/todo/{id}')
async def get_todo(id: int = Path(..., title="The id of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == id:
            return {"todo": todo}
    return {"msg": "Provided todo id doesn't exist."}


@todo_router.put('/todo/{id}')
async def update_todo(todo_task: TodoTask, id: int = Path(..., title="The id of the todo to update.")) -> dict:
    for todo in todo_list:
        if todo.id == id:
            todo.task.task = todo_task.task
            print(todo.task.task, todo_task.task)
            return {"msg": "Todo Task updated successfully."}  
    return {"msg": "Provided todo id doesn't exist."}

@todo_router.delete('/todo/{id}')
async def delete_single_todo(id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[id]
        if todo.id == id:
            todo_list.pop(index)
            return {"msg": "Todo Task deleted successfully."}
    return {"msg": "Provided todo id doesn't exist"}

@todo_router.delete('/todo')
async def delete_all_todo() -> dict:
    if len(todo_list) != 0:
        todo_list.clear()
        return {"msg": "All Todo Tasks deleted successfully."}
    return {"msg": "No more todo tasks to delete."}