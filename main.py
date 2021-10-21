from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'message': "Hello, world!"}

@app.get('/alternativa')
def alt():
    return {'message': "Este es otro endpoint"}

@app.get('/alt/{id}')
def alt_id(id):
    return {'id': int(id)*2}