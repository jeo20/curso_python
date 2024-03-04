from fastapi import APIRouter, HTTPException # Importamos FastApi
from pydantic import BaseModel # Importamos la clase base de PyDantic para crear nuestra propia clase.

router = APIRouter(prefix="/users", #  Establecemos el prefijo que tendrá esta ruta, es "/users"
                   tags=["users"], #  Agregamos una etiqueta a este grupo de rutas, en este caso "products". Se utiliza para agrupar las rutas relacionadas
                   responses={404: {"message": "No encontrado"}}) # mensaje de error con status code

"""

DEFINICION DE ROUTER
********************
* Importo ApiRouter
* creo una instancia de APIRouter
* Nombro @router.(el metodo que necesitemos, get, post, put, delete)('/ruta')

"""

### ENTIDAD USER ###
class User(BaseModel): # Creación de la clase "User" heredando de BaseModel, que implementa las validaciones
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id=1, name="JeO", surname="Orellana", url="https://www.infobae.com/", age=45),
              User(id=2, name="Pedro", surname="Orellana", url="https://www.ole.com.ar/", age=40),
              User(id=3, name="Juan", surname="Orellana", url="https://www.tiemposur.com.ar/", age=35)]


@router.get("/usersjson") # Decorador para definir una ruta GET en /usersjson
async def usersjson(): #  Es una función asincrona, por lo que se utiliza "async"
    return [{"name": "JeO", "surname": "Orellana", "url": "https://www.infobae.com/", "age": 45},
            {"name": "Pedro", "surname": "Orellana", "url": "https://www.ole.com.ar/", "age": 40},
            {"name": "Juan", "surname": "Orellana", "url": "https://www.tiemposur.com.ar/", "age": 35}]



# METODO GET PATH  recomendado para parametros fijos
@router.get('/users/')
async def users():
    return users_list

# METODO GET PATH  recomendado para parametros fijos
@router.get('/user/{id}')
async def user(id: int):
    return search_user(id)


# METODO GET QUERY recomendado para parametros dinamicos
@router.get("/userquery/")
async def user(id: int):
    return search_user(id)


# METODO POST CREAR USUARIO
@router.post('/user/', response_model=User, status_code=201) #  Ruta POST en /user/
async def user(user: User): #  El nombre del parámetro debe ser igual al nombre de la clase
        if type(search_user(user.id)) == User: # Compruebo si el usuario existe antes de crearlo
            raise HTTPException(status_code=404, detail="El usuario ya existe") #  Si el usuario existe lanza error 404
        else:            
            users_list.append(user) # Si el usuario no existe lo crea correctamente
            return user
        
        
# METODO PUT MODIFICAR USUARIO
@router.put('/user/')  # Ruta PUT en /user/
async def user(user: User):   # Recibe un objeto User con los datos a modificar
    found = False   # Bandera para saber si se ha encontrado al usuario
    for index, saved_user in enumerate(users_list):  # Recorrido de la lista de usuarios
        if saved_user.id == user.id:   # Pregunto si existe el usuario
            users_list[index] = user   # Modifico los datos del usuario existente con los nuevos
            found = True    # Marco como encontrado y salgo del bucle            
    if not  found:   # Si no ha encontrado el usuario (es nuevo)
        return {"error": "Usuario no actualizado"}
    else:         # Devuelvo el mensaje de confirmación de modificación
        return user

# METODO DEL ELIMINAR USUARIO
@router.delete('/user/{id}')   # Ruta DELETE en /user/
async def user(id: int):    # No recibe parámetros, se utiliza para eliminar todos los usuarios
    found = False   # Bandera para saber si se ha encontrado al usuario    
    for index, saved_user in enumerate(users_list):  # Recorrido de la lista de usuarios
        if saved_user.id == id:   # Pregunto si existe el usuario
            del users_list[index] # Modifico los datos del usuario existente con los nuevos
            found = True    # Marco como encontrado y salgo del bucle  
    if not  found:   # Si no ha encontrado el usuario (es nuevo)
        return {"error": "No se ha eliminado el usuario"}
    else:         # Devuelvo el mensaje de confirmación de modificación
        return {"Usuario eliminado correctamente"}       
            
        


#### DEFINICION DE CLASES ####
##############################

#### CLASE BUSCA USUARIO
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
