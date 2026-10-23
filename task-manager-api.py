from fastapi import FastAPI, HTTPException, status, Path
from pydantic import BaseModel, Field
from typing import Optional 

app = FastAPI()

class Task(BaseModel):
  id: int = Field(gt=0)
  Title: str
  Completed: bool = False

class CreateTask(BaseModel):
  Title: str
  Completed: bool = False

class UpdateTask(BaseModel):
  Title: Optional[str] = None
  Completed: Optional[bool] = None

class TaskCreatedResponse(BaseModel):
  message: str

tasks = [
  {
      "id": 1,
      "Title": "Create an API",
      "Completed": True
  },
  {
      "id": 2,
      "Title": "Learn python",
      "Completed": False
  }
]

@app.get("/task_manager_api/tasks", response_model = list[Task])
def get_tasks():
    return tasks

@app.get("/task_manager_api/tasks/{task_id}", response_model = Task)
def get_tasks_with_id(task_id: int = Path(gt=0)):
  for task in tasks:
    if task["id"] == task_id:
      return task

  raise HTTPException(status_code = 404, detail = "No task found with that ID.")

@app.post("/task_manager_api/tasks", status_code = status.HTTP_201_CREATED, response_model = TaskCreatedResponse)
def create_task(new_task: CreateTask):
  task_id = max((task["id"] for task in tasks), default=0) + 1

  task = {
      "id": task_id,
      "Title": new_task.Title,
      "Completed": new_task.Completed
  }

  tasks.append(task)

  return {"message": "New task created successfully."}

@app.patch("/task_manager_api/tasks/{task_id}", response_model = Task)
def update_task(task: UpdateTask, task_id: int = Path(gt=0)):
  for existing_task in tasks:
    if existing_task["id"] == task_id:
      update_data = task.model_dump(exclude_unset=True)
      existing_task.update(update_data)
      return existing_task

  raise HTTPException(status_code=404, detail="No task found with that ID.")

@app.delete("/task_manager_api/tasks/{task_id}")
def delete_task(task_id: int = Path(gt=0)):
  for task in tasks:
    if task["id"] == task_id:
      tasks.remove(task)
      return {"Message": f"Task {task_id} deleted successfully"}  

  raise HTTPException(status_code=404, detail="No task found with that ID.")
