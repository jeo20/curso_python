from fastapi import FastAPI # importando fastapi
from pydantic import BaseModel #importando la clase  base de pydantic para crear nuestra propia clase

app = FastAPI() # creando instancia de FastAPI llamada app

# Inicia el server: uvicorn users:app --reload

# Url local: http://127.0.0.1:8000/users
@app.get("/users") # decorador  que indica a FastAPI que este es un metodo GET y va a estar en la ruta /users
async def users(): # esta funcion se ejecutara cuando hagamos una peticion get a /users
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]