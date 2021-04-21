from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Boolean, Column, Integer, String
from fastapi import FastAPI

engine = create_engine("sqlite:///./sql_app.db", echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)

app = FastAPI()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


@app.get("/")
def read_root():
    return {"Hello": "World"}