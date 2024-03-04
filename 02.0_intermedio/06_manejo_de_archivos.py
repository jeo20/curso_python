# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=15524

### File Handling ###

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("02_intermedio/my_file.txt", "w+", encoding="utf-8")

txt_file.write(
    "Mi nombre es Jorge\nMi apellido es Orellana\n45 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Cobol")
print(txt_file.readline())

txt_file.close()

with open("02_intermedio/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Visual Fox Pro")

# os.remove("Intermediate/my_file.txt")


# Clase en vídeo (03/11/22): https://www.twitch.tv/videos/1642512950

# .json file

json_file = open("02_intermedio/my_file.json", "w+")

json_test = {
    "name": "Jorge Eduardo",
    "surname": "Orellana",
    "age": 45,
    "languages": ["Python", "Cobol", "Visual Fox Pro"],
    "website": "https://jeodev.com.ar"}

json.dump(json_test, json_file, indent=2)
 # metodo dump escribe  el diccionario completo en el archivo json
 # necesita 2 parametros, el primero es el diccionario a guardar
 # el segundo es el fichero donde se va a guardar
 # el tercero es la cantidad de espacios que van a separar los elementos del diccionario
 # opcionalmente puedes pasar un tercer parametro que indica la cantidad de espacios para cada nivel de indentación

json_file.close() #  cerrar el fichero una vez terminado de trabajar con él

with open("02_intermedio/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("02_intermedio/my_file.json")) #  Cargamos el contenido del json y lo convertimos en un diccionario
print(json_dict)
print(type(json_dict))
print(json_dict["name"])


# .csv file

csv_file = open("02_intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Jorge", "Orellana", 45, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("02_intermedio/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?