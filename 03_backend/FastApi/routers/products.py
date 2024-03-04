# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=12475

### Products API ###

from fastapi import APIRouter # Importamos la clase Router de FastAPI para crear nuestra API

router = APIRouter(prefix="/products", #  Establecemos el prefijo que tendrá esta ruta, es "/products"
                   tags=["products"], #  Agregamos una etiqueta a este grupo de rutas, en este caso "products". Se utiliza para agrupar las rutas relacionadas
                   responses={404: {"message": "No encontrado"}}) #  Agregamos una respuesta personalizada a un error HTTP 404 Not Found

products_list = ["Producto 1", "Producto 2",
                 "Producto 3", "Producto 4", "Producto 5"]


@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]