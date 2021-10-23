# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

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

@app.get('/alt/{id}')
def alt_id(id):
    return {'id': int(id)}

# Request and response body
@app.post('/person/new')
def new_person(persona: Person = Body(...)):
    return persona

# Validaciones query parameters
@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title='Person Name',
        description='This is the person name'
        ), 
    age: int = Query(
        ...,
        title='Person Age',
        description='This is the person age'
        )
    ):

    return {name: age}

# Validaciones path parameters
@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title='Person Id',
        description='This is the Person Id'
        )
    ):

    return {person_id: 'Succesfull'}