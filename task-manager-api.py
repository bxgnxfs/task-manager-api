from fastapi import FastAPI, HTTPException, status, Path
from pydantic import BaseModel, Field
from typing import Optional 

app = FastAPI()

class Task(BaseModel):
  id: int = Field(gt=0)
  Title: str
  Completed: bool = False

class UpdateTask(BaseModel):
  Title: Optional[str] = None
  Completed: Optional[bool] = None

tasks = {
   1:{
      "id": 1,
      "Title": "Create an API",
      "Completed": True
    },
   2:{
      "id": 2,
      "Title": "Learn python",
      "Completed": False
    }
}

@app.get("/task_manager_api/tasks")
def get_tasks():
    return tasks

@app.get("/task_manager_api/tasks/{task_id}")
def get_tasks_with_id(task_id: int = Path(gt=0)):
  if task_id not in tasks:
    raise HTTPException(status_code = 404, detail = "No task found with that ID.")

  return tasks[task_id]

@app.post("/task_manager_api/tasks", status_code = status.HTTP_201_CREATED)
def create_task(new_task: Task):
  if new_task.id in tasks:
    raise HTTPException(status_code = 404, detail = "A task with that ID already exists.")

  tasks[new_task.id] = new_task.model_dump()
  return tasks[new_task.id]

@app.patch("/task_manager_api/tasks/{task_id}")
def update_task(task: UpdateTask, task_id: int = Path(gt=0)):
  if task_id not in tasks:
    raise HTTPException(status_code = 404, detail = "No task found with that ID.")
  
  update_data = task.model_dump(exclude_unset = True)

  tasks[task_id].update(update_data)
  
  return tasks[task_id]

@app.delete("/task_manager_api/tasks/{task_id}")
def delete_task(task_id: int = Path(gt=0)):
  if task_id not in tasks:
    raise HTTPException(status_code = 404, detail = "No task found with that ID.")

  del tasks[task_id]
  return {"Message": f"Task {task_id} deleted succefully"}   