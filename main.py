# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()

# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

# Routes

@app.get('/')
def home():
    return {'message': "Hello, world!"}

@app.get('/alternativa')
def alt():
    return {'message': "Este es otro endpoint"}

@app.get('/alt/{id}')
def alt_id(id):
    return {'id': int(id)}

# Request and response body
@app.post('/person/new')
def new_person(persona: Person = Body(...)):
    return persona

# Validaciones
@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50), 
    age: str = Query(...)
    ):

    return {name: age}
