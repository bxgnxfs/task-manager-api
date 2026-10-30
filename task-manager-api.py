from fastapi import FastAPI, HTTPException, status, Path
from sqlalchemy import select

from models import Task, UpdateTask, CreateTask, TaskCreatedResponse, TaskResponse
from database import Base, engine, SessionDep

app = FastAPI()

def create_db_tables():
  Base.metadata.create_all(bind = engine)

@app.on_event("startup")
def on_startup():
  create_db_tables()

@app.get("/task-manager-api/tasks", response_model = list[TaskResponse])
def get_tasks(session: SessionDep):
  all_tasks = session.scalars(select(Task)).all()

  return all_tasks

@app.get("/task-manager-api/tasks/{task_id}", response_model = TaskResponse)
def get_tasks_with_id(task_id: int, session: SessionDep):
  task = session.get(Task, task_id)
  if not task:
    raise HTTPException(status_code = 404, detail = "No task found with that ID.")
  
  return task

@app.post("/task-manager-api/tasks", status_code = status.HTTP_201_CREATED, response_model = TaskCreatedResponse)
def create_task(new_task: CreateTask, session: SessionDep):
  task = Task(
    Title=new_task.Title,
    Completed=new_task.Completed
  )
  
  session.add(task)
  session.commit()
  session.refresh(task)

  return {"message": "New task created successfully."}

@app.patch("/task-manager-api/tasks/{task_id}", response_model = TaskResponse)
def update_task(update_task: UpdateTask, task_id: int, session: SessionDep):
  task = session.get(Task, task_id)

  if not task:
    raise HTTPException(status_code=404, detail="No task found with that ID.")

  update_data = update_task.model_dump(exclude_unset=True)
    
  for field, value in update_data.items():
    if value is not None:
      setattr(task, field, value)
    
  session.commit()
  session.refresh(task)

  return task

@app.delete("/task-manager-api/tasks/{task_id}")
def delete_task(task_id: int, session: SessionDep):
  task = session.get(Task, task_id)

  if not task:
    raise HTTPException(status_code=404, detail="No task found with that ID.")

  session.delete(task)
  session.commit()

  return {"Message": f"Task {task_id} deleted successfully"}  

  
