# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=24010

### Python Package Manager ###

# PIP https://pypi.org

# pip install pip
# pip --version

# pip install numpy
import pandas
from mypackage import arithmetics #  Importar un módulo arithmetics de mi propio paquete(mypackage)
import requests #  Librería para hacer solicitudes HTTP
import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip install pandas

# pip list
# pip uninstall pandas
# pip show numpy

# pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response) #  Mostrar la respuesta completa
print(response.status_code) #  Estatus del request (si fue exitoso o no)
print(response.json()) # Mostrar el contenido como diccionario


# Arithmetics Package 

print(arithmetics.sum_two_values(1, 4)) # llama al modulo arithmetics  y a su función sum_two_values con los valores 1 y 4
