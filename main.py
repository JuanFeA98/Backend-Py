# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path
from pydantic.schema import schema

app = FastAPI()

# Models

class HairColor(Enum):
    white= 'white'
    brown= 'brown'
    black= 'black'
    blonde= 'blonde'
    red= 'red'


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    age: int = Field(
        ...,
        gt=0,
        le=115
        )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

    class Config:
        schema_extra = {
            'example': {
                'first_name': 'Sandra',
                'last_name': 'Martínez',
                'age': 13,
                'hair_color': 'brown',
                'is_married': False
            }
        }


class Location(BaseModel):
    city: str
    state: str
    country: str

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

# Validaciones request body 
@app.put('/person/{person_id}')
def update_person(
    person_id: int = Path(
            ...,
            gt=0,
            title='Person id',
            description='This is the Person Id'
        ),
        person: Person=Body(...),
        # location: Location=Body(...)
    ):
    
    # results = person.dict()
    # results.update(location.dict())

    return person