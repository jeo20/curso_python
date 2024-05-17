# # def hola():
# #     return "¡Hola!"

# # def hazEstoAntesDeHola(func):
# #     print("Hacer algo antes de llamar a func")
# #     print(func())

# # hazEstoAntesDeHola(hola)
# # #Salida: Hacer algo antes de llamar a func
# # #        ¡Hola!

# def nuevo_decorador(a_func):

#     def envuelveLaFuncion():
#         print("Haciendo algo antes de llamar a a_func()")

#         a_func()

#         print("Haciendo algo después de llamar a a_func()")

#     return envuelveLaFuncion

# def funcion_a_decorar():
#     print("Soy la función que necesita ser decorada")

# funcion_a_decorar()
# #Salida: "Soy la función que necesita ser decorada"

# funcion_a_decorar = nuevo_decorador(funcion_a_decorar)
# #Ahora funcion_a_decorar está envuelta con el decorador que hemos creado

# funcion_a_decorar()
# #Salida: Haciendo algo antes de llamar a a_func()
# #        Soy la función que necesita ser decorada
# #        Haciendo algo después de llamar a a_func()

import numpy as np


def restar_movimientos(array):
    # Crear una copia del array para no modificar el original
    resultado = array.copy()
    # Obtener las dimensiones del array
    filas, columnas = array.shape
    
    # Iterar sobre cada elemento del array
    for i in range(filas):
        for j in range(columnas):
            if array[i, j] > 0:
                # Verificar y restar 1 a los elementos adyacentes
                if i > 0:  # Arriba
                    resultado[i - 1, j] = max(0, resultado[i - 1, j] - 1)
                if i < filas - 1:  # Abajo
                    resultado[i + 1, j] = max(0, resultado[i + 1, j] - 1)
                if j > 0:  # Izquierda
                    resultado[i, j - 1] = max(0, resultado[i, j - 1] - 1)
                if j < columnas - 1:  # Derecha
                    resultado[i, j + 1] = max(0, resultado[i, j + 1] - 1)
    
    return resultado

# Ejemplo de uso
array = np.array([[2, 1, 0],
                  [5, 5, 1],
                  [1, 0, 2]])

print("Array original:")
print(array)

resultado = restar_movimientos(array)
print("Array resultado:")
print(resultado)
