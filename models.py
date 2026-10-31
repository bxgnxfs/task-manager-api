from sqlalchemy import Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pydantic import BaseModel, ConfigDict
from database import Base

class Task(Base):
  __tablename__ = "tasks"

  id: Mapped[int] = mapped_column(Integer, primary_key = True)
  Title: Mapped[str] = mapped_column(String, nullable = False)
  Completed: Mapped[bool] = mapped_column(Boolean, nullable = False, default = False)

  user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable = True)

  user: Mapped["User | None"] = relationship(back_populates = "tasks")

class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(Integer, primary_key = True)
  username: Mapped[str] = mapped_column(String(50), unique = True, nullable = False)

  tasks: Mapped[list["Task"]] = relationship(back_populates = "user")

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

class CreateUser(BaseModel):
    username: str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    tasks: list[TaskResponse]
