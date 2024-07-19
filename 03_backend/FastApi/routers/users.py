from fastapi import APIRouter, HTTPException  # importando fastapi
from pydantic import \
    BaseModel  # importando la clase BaseModel de pydantic para crear nuestra propia clase

# uvicorn users:app --reload

router = APIRouter(prefix="/users", tags=["users"], responses={404: {"message": "No encontrado"}}) # creando instancia de FastAPI llamada app

# Entidad User
class User(BaseModel): # Creo clase User heredada de BaseModel con 4 atributos (name, surname, url y age)
    id: int
    name: str
    surname: str
    url: str
    age: int

# Creo una lista de usuarios
users_list = [User(id=1, name="BraisL", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="MoureL", surname="Dev", url="https://mouredev.com", age=35),
              User(id=3, name="Jorge", surname="Orellana", url="https://jeo.com", age=46)]

#url local: http://127.0.0.1:8000/users
@router.get("/usersjson") # decorador que indica a FastAPI que este es un metodo GET y que va a estar en la ruta /users
async def usersjson():  # Creamos un JSON de la lista de usuarios
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]
    
#url local: http://127.0.0.1:8000/users
@router.get("/users") # decorador que indica a FastAPI que este es un metodo GET y que va a estar en la ruta /users
async def users():  # Creamos un JSON de la lista de usuarios
    return users_list # retorna el contenido de la lista user_list

#Path: http://127.0.0.1:8000/user/id
@router.get("/user/{id}") # decorador que indica a FastAPI que este es un metodo GET y que va a estar en la ruta /user/id
async def user(id:int):  # Creamos un JSON con el id definido en path
    return search_user(id)
    

#Query: http://127.0.0.1:8000/userquery/
@router.get("/userquery/") # decorador que indica a FastAPI que este es un metodo GET y que va a estar en la ruta /userquery/
async def user(id:int):  # Creamos un JSON con el id definido en path
    return search_user(id)
    
# Post Graba POST http://127.0.0.1:8000/user
@router.post("/user/", response_model=User, status_code=201) # decorador de post en la ruta user
async def user(user: User): # funcion user que recibe un usuario de la entidad User
    if type(search_user(user.id)) == User: # compruebo si el usuario existe para no duplicarlo
        raise HTTPException(status_code=404, detail="El usuario ya existe")    
    users_list.append(user) # si no existe lo agrego a la lista de usuarios
    return user
    
 
# Put Actualiza PUT http://127.0.0.1:8000/user/
@router.put("/user/") # decorador de post en la ruta user
async def user(user: User): # funcion user que recibe un usuario de la entidad User
    found = False # creo la variable found y la inicializo como False
    for index, saved_user in enumerate(users_list): # indexo el la lista para enumerar y saber la posicion del usuario en la lista
        if saved_user.id == user.id: # busca si el id del usuario existe en la lista
            users_list[index] = user # actualizo el usuario
            found = True # si actualizo el usuario cambio found a True
    if not found: # si found no es True muestra el mensaje de error
        return {"error": "No se ha actualizado el usuario"} # mensaje error si no puede actualizar el usuario
    return user # devuelvo el usuario actualizado
    
# Delete Elimina DELETE http://127.0.0.1:8000/user/4
@router.delete("/user/{id}") # decorador de delete en la ruta user
async def user(id:int):
    found = False
    for index, saved_user in enumerate(users_list): # indexo el la lista para enumerar y saber la posicion del usuario en la lista
        if saved_user.id == id: # busca si el id del usuario existe en la lista
            del users_list[index] # elimino el usuario
            found = True # si elimino el usuario cambio found a True            
    if not found: # si found no es True muestra el mensaje de error
        return {"Error": "No se ha eliminado el usuario"} # mensaje error si no puede eliminar el usuario

            
# Funcion que busca el id del usuario
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list) # filtro para encontrar el id especifico con funcion lambda
    try:
        return list(users)[0] # devuelve el id buscado en el path
    except:
        return {"Error": "No se ha encontrado el usuario"} # mensaje error de excepcion
    