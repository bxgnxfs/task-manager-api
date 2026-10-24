from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

database_url = "sqlite:///Task.db"
engine = create_engine(database_url, connect_args = {"check_same_thread": False})

Session = sessionmaker(autocommit = False, autoflush = False, bind = engine)

class Base(DeclarativeBase):
    pass

def get_session():
    with Session() as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]