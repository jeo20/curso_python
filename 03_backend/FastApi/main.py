from fastapi import FastAPI  # importando fastapi
from fastapi.staticfiles import StaticFiles  # importo para recursos estaticos
from routers import basic_auth_users, jwt_auth_users, products, users, users_db

app = FastAPI() # creando instancia de FastAPI llamada app

# Routers
app.include_router(products.router) # incluyendo el router de products en app

app.include_router(users.router) # incluyendo el router de users en app

app.include_router(users_db.router)

app.include_router(basic_auth_users.router)

app.include_router(jwt_auth_users.router)

#app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Url local: http://127.0.0.1:8000
@app.get("/") # decorador para definir la ruta y el metodo http que va a responder a esa ruta, en este caso es GET
async def root(): # definicion de la ruta raiz, es decir, cuando se accede a http://localhost:8000/ (funcion asincrona)
    return {"message": "Hola JeO desde Main"} # retornar un json(clave:valor) con el mensaje "Hola JeO"


# Url local: http://127.0.0.1:8000/url
@app.get("/url")  # decorador @ que indica que la función es una ruta GET http://localhost:8000/url
async def url(): # definición de la función asincrona url
    return {"url": "https://mouredev.com/python"} # retornar un json con la clave "url" y su valor como URL