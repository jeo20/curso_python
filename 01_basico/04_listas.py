# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###
"""
La lista, la cual puede ser escrita como una lista de valores separados por coma (ítems) entre corchetes. 
Las listas pueden contener ítems de diferentes tipos, pero usualmente los ítems son del mismo tipo.
lista_ejemplo = [1, 4, 9, 16, 25]

"""
# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

#Lista con distinto tipos de datos
my_other_list = [45, 1.85, "Jorge", "Orellana"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda
# 0 es el primer elemento de la lista
# -1 es el ultimo elemento de la lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
# .count() devuelve el numero de ocurrencia adentro de una lista
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Orellana"))

#desempaquetado de variables a lista
age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

# Agrega 1 elemento al final de una lista
my_other_list.append("JeODev")
print(my_other_list)

# Agrega 1 elemento en una posicion especifica
my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

# Elimina el primer elemento  especificado de una lista
my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

# pop() elimina el ultimo elemento de una lista y lo mantiene en memoria
print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

# copia una lista
my_new_list = my_list.copy()

# vacia una lista
my_list.clear()
print(my_list)
print(my_new_list)

# ordena en orden inverso una lista
my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))