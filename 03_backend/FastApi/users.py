from fastapi import FastAPI # importando fastapi
from pydantic import BaseModel #importando la clase BaseModel de pydantic para crear nuestra propia clase

app = FastAPI() # creando instancia de FastAPI llamada app

# Inicia el server: uvicorn users:app --reload

class User(BaseModel): # Creo clase User heredada de BaseModel con 4 atributos (name, surname, url y age)
    name: str
    surname: str
    url: str
    age: int

# Creo una lista de usuarios
users_list = [User(id=1, name="BraisL", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="MoureL", surname="Dev", url="https://mouredev.com", age=35),
              User(id=3, name="BraisL", surname="Dahlberg", url="https://haakon.com", age=33)]
       
# Url local: http://127.0.0.1:8000/users
@app.get("/usersjson") # decorador  que indica a FastAPI que este es un metodo GET y que va a estar en la ruta /users
async def users(): # esta funcion se ejecutara cuando hagamos una peticion get a /users
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]

#url local: http://127.0.0.1:8000/userclass
@app.get("/users") # decorador que indica a FastAPI que este es un metodo GET y que va a estar en la ruta /usersclass
async def users():  # Creamos un JSON de la lista de usuarios
    return users_list # retorna el contenido de la lista user_list
#    return User(name ="Brais", surname="Moure", url="https://moure.dev", age=35) # llama a la clase User y retorna el usuario Brais