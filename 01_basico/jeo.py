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