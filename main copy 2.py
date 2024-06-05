from fastapi import FastAPI,status,Response
from typing import Optional

app=FastAPI()

users=[
    {
    "id": 1,
    "nombre":"Ronnie",
    "apellido":"Alvarez",
    "edad":55
    },
    {
    "id":2 ,
    "nombre":"Maria E",
    "apellido":"Leon",
    "edad":53
    }
    ]


@app.get('/')
def message():
    return 'Hola mundo!!! Hello'

@app.get('/users')
def get_users():
    return users

@app.get('/user/{id}')
def get_user(id,nombre:Optional[str]=None):
    for user in users:
        if user['id']==int(id) and user['nombre']==nombre:
            return user
    return {"menssage":"Usuario no encontrado"}

@app.get('/welcome/{nombre}/{apellido}',status_code=status.HTTP_201_CREATED)
def mensaje(nombre:str,apellido:str)-> str:
    return f"Bienvenido {nombre.upper()} {apellido.upper()}"

@app.get('/saludo/{nombre}/{apellido}')
def mensaje(nombre:str,apellido:str,response: Response):
    if len(nombre)>0 and len(apellido)>0:
        response.status_code=status.HTTP_202_ACCEPTED
    else:
        response.status_code=status.HTTP_400_BAD_REQUEST
