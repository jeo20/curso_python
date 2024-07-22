from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter(prefix="/basicauth",
                   tags=["basicauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login") # instancia de oauth2 se define la url encargada de la autenticacion

# Clase Usuario
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
# Clase UserDb    
class UserDB(User): # UserDB hereda de la clase User
    password: str

    
users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mourede.com",
        "disabled": False,
        "password": "123456"
    },
    "jeo": {
        "username": "jeo",
        "full_name": "jorge orellana",
        "email": "jeo@jeo.com",
        "disabled": True,
        "password": "654321"
    }
}

# funcion para buscar el usuario en la base de datos    
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username]) # devuelve usuario de base de datos
    
def search_user(username: str): # funcion search_userque recibe de parametro el username
    if username in users_db: # busca el username en la base de datos
        return User(**users_db[username]) # retorna el usuario encontrado

    
# funcion current_user criterio de dependencia
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token) # busca el token(username)
    if not user: # si el usuario no tiene permiso
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})

    if user.disabled: # si el usuario esta desactivado
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")

    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()): # recibe datos pero no depende de nadie
    user_db = users_db.get(form.username) # almaceno el usuario para buscarlo
    if not user_db:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username) # busco el usuario en la base de datos
    
    if not form.password == user.password: # compruebo la contraseña si es correcta
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
     
    # devuelve un token(username) cuando el usuario y la contraseña son correctos   
    return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user


