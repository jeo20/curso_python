"""
Los decoradores en Python son funciones que modifican el comportamiento de otras funciones. 
Se pueden usar para agregar funcionalidades a las funciones existentes sin tener que modificar su código original.
"""
# def decorador(funcion):
#     def funcion_modificada():
#         print("Antes de llamar a la funcion")
#         funcion() #  Llamamos a la función original
#     return  funcion_modificada 

# @decorador 
# def saludo():
#     print("Hola, soy un saludo")

# saludo()
# # Salida: Antes de llamar a la función Hola, soy un saludo  

def mi_decorador(funcion): #  funcion mi_decorador que recibe funcion como parametro
    def funcion_decorada(*args, **kwargs): # *args y **kwargs permiten pasar cualquier cantidad de argumentos a la función
        print("Antes de la función")
        funcion(*args, **kwargs) # Recibe el nombre de la funcion decorada saludar
        print("Después de la función")
    return funcion_decorada

@mi_decorador # Decoramos la función saludar
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("JeO 2024")
