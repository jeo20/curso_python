from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # Clase que se encarga de administrar la autenticacion

app = FastAPI() # Creamos la instancia de FastApi

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
class UserDB(User):
    password: str
    
    
users_db = {
    "jeo": {
        "username": "jeo",
        "full_name": "Jorge Orellana",
        "email": "jeo@jeo.com",
        "disabled": False,
        "password": "123456"
    },
    "jeo2": {
        "username": "jeo2",
        "full_name": "Jorge Orellana 2",
        "email": "jeo2@jeo2.com",
        "disabled": True,
        "password": "987654"
    }
}

# FUNCION QUE BUSCA  USUARIO EN LA BBDD Y RETORNA UN OBJETO DEL MODELO USER DB
def search_user_db(username: str): # funcion para buscar  un usuario en la base de datos
    if username in users_db: #  si el nombre de usuario existe devuelve el diccionario del usuario
        return UserDB(**users_db[username]) #  Retornamos un objeto UserDB con los datos del usuario buscado
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user
    
###### FUNCION QUE COMPRUEBA USUARIO Y CLAVE ######
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()): # Establecemos que form es una dependencia y se le pasa como parametro a async def login
    user_db = users_db.get(form.username) #  Buscamos el usuario en la base de datos (user_db)
    if not user_db: #  Si no lo encontró significa que el usuario no está registrado
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto") # Mensaje de error de usuario

    user = search_user_db(form.username) #  Buscamos el usuario en la base de datos (user_db)
    if not form.password == user.password: # Comprueba la contraseña
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta") # Mensaje de error de contraseña

    return {"access_token": user.username, "token_type": "bearer"} #  Devuelve un token de acceso al usuario autenticado tipo bearer

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user