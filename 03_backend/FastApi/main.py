from fastapi import FastAPI # importando fastapi

app = FastAPI() # creando instancia de FastAPI llamada app

# Url local: http://127.0.0.1:8000
@app.get("/") # decorador para definir la ruta y el metodo http que va a responder a esa ruta, en este caso es GET
async def root(): # definicion de la ruta raiz, es decir, cuando se accede a http://localhost:8000/ (asincrona)
    return {"message": "Hola JeO"} # retornar un json(clave:valor) con el mensaje "Hola JeO"

"""
# Url local: http://127.0.0.1:8000/url
@app.get("/url")  # decorador @ que indica que la función es una ruta GET http://localhost:8000/url
async def url(): # definición de la función asincrona url
    return {"url": "https://mouredev.com/python"} # retornar un json con la clave "url" y su valor como URL
"""