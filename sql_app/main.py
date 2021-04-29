from fastapi import FastAPI
from database import engine
from models import model

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

