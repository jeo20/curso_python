# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=1810

### Type Hints ###
"""
Desde la versión 3.5 de Python existe algo que se llama type hints y que nos permiten poner tipos a variables, listas, funciones, etc.

Sin embargo tal como el nombre indica es solo una sugerencia y por tanto el interprete no las va a tener en cuenta.
"""

my_string_variable = "My String variable"
print(my_string_variable)
print(f"{type(my_string_variable)}\n")

my_string_variable = 5
print(my_string_variable)
print(f"{type(my_string_variable)}\n")

#my_typed_variable: int = "My typed String variable" #sigue siendo un string por mas que lo declare como entero y se habilitan los metodos de enteros
#my_typed_variable.round(number[, ndigits]) -> float # usa metodos para numeros
my_typed_variable: str = "My typed String variable"
print(my_typed_variable)
print(f"{type(my_typed_variable)}\n")

my_typed_variable = 5
print(my_typed_variable)
print(f"{type(my_typed_variable)}\n")