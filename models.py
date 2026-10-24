from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel, ConfigDict
from database import Base

class Task(Base):
  __tablename__ = "tasks"

  id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
  Title: Mapped[str] = mapped_column(String, nullable = False)
  Completed: Mapped[bool] = mapped_column(Boolean, nullable = False, default = False)

class TaskResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: int
  Title: str
  Completed: bool

class UpdateTask(BaseModel):
  Title: str | None = None
  Completed: bool | None = None

class CreateTask(BaseModel):
  Title: str 
  Completed: bool = False

class TaskCreatedResponse(BaseModel):
  message: str