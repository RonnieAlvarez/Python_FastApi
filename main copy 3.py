from fastapi import FastAPI,status,Response,HTTPException,Request,Depends
from typing import Optional,List
from models.Developer import Developer
from fastapi.responses import PlainTextResponse,JSONResponse
import jwt

app=FastAPI()
is_logged=True
developers=[]

users=[{
    "username":"admin",
    "password":"123456"
}]
# developers = [ { "id": 1, "name": "Pablo España", "country": "Ecuador", "age": 26,
# "experience": [ { "title": "Software Developer", "location": "Ecuador", "start_date": "2021",
# "end_date": "Present", "organization": "Real Company" } ], "skills": [ { "name": "Python", "years": 5 }, 
# { "name": "JavaScript", "years": 6 }, { "name": "React", "years": 2 }, ], "languages":[ { "name": "Spanish", 
# "level": "Native" }, { "name": "English", "level": "Intermediate" } ] } ]

@app.middleware("http")
async def check_logged(request:Request,call_next):
    if is_logged:
        response= await call_next(request)
        return response
    return JSONResponse(content={"message":"No autorizado, Inicie sesion"},status_code=401)

@app.middleware("http")
def my_middleware(request:Request,call_next):
    print(f'Accediendo a la ruta: {request.url}')
    response= call_next(request)
    return response

def verify_token(request: Request):
    token=request.headers['Authorization']
    data = jwt.decode(token,"My_Secret",algorithms=["HS256"])
    for user in users:
        if user['username']==data['username']:
            return True
    return False

@app.post('/login')
def login(username:str,password: str):
    for user in users:
        if user['username']==username and user['password']==password:
            return jwt.encode(user,"My_Secret",algorithm="HS256")
    return "datos incorecctos"


@app.get('/developers')
def get_developers(authorized:bool = Depends(verify_token)):
    if authorized:
        return developers
    else:
        return "No autorizado"

@app.get('/developers/{id}')
def get_developers(id: int):
    for developer in developers:
        if developer.id==id:
            return developer
    return "No encontrado"
            
@app.get('/developers/{id}/skills')
def get_developer(id:int):
    for developer in developers:
        if developer.id == int(id):
            return developer.skills
    return "No encontrado"
        
            
@app.get('/developers/{id}/experience')
def get_developer(id:int):
    for developer in developers:
        print(developer)
        print(type(developer))
        print(type(developers))
        if developer.id==id:
            return developer.experience
    return "No encontrado"
            
@app.get('/developers/{id}/languages')
def get_developer(id:int):
    for developer in developers:
        if developer.id==id:
            return developer.languages
    return "No encontrado"
            
@app.post('/developers')
def create_developer(developer:Developer):
    if len(developer.name)>5:
        raise HTTPException(status_code=400,detail="Nombre no puede tener mas de 5 caracteres")
    if developer.age>100:
        raise HTTPException(status_code=400,detail="Edad incorrecta")
    developers.append(developer)
    if len(developer.skills)==0:
        raise HTTPException(status_code=400,detail="Se requieren Habilidades")
    # return PlainTextResponse(status_code=201,content="Registro Correcto")
    return JSONResponse(status_code=201,content={"message":"Registro Correcto"})

@app.delete('/developers/{id}')
def delete_developer(id: int):
    for developer in developers:
        if developer.id==id:
            developers.remove(developer)
            return developers
    return "Developer Not Found: "

@app.put('/developers/{id}')
def update_developers(data: Developer, id: int):
    for developer in developers:
        if developer.id== id:
            developer.name = data.name
            developer.country=data.country
            developer.age = data.age
            developer.experience = data.experience
            developer.skills = data.skills
            developer.languages = data.languages
            return developer
    return "No encontrado"
            