from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of the FastAPI app
app = FastAPI()

# Task model to accept data in the body of the POST request
class Task(BaseModel):
    name: str
    done: bool = False

# In-memory task store (we'll use a simple list for now)
tasks = [{"id": 1, "name": "Do homework", "done": False}]

# Define a simple GET route at the root URL
@app.get("/")
def read_root():
    return {"message": "Welcome to your Task Manager API!"}

# Define another GET route to get some sample tasks
@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

# POST route to create a new task
@app.post("/tasks")
def create_task(task: Task):
    new_task = {"id": len(tasks) + 1, "name": task.name, "done": task.done}
    tasks.append(new_task)
    return new_task

# PUT route to update a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for t in tasks:
        if t["id"] == task_id:
            t["name"] = task.name
            t["done"] = task.done
            return t
    return {"error": "Task not found"}

# DELETE route to delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": f"Task {task_id} deleted successfully"}
