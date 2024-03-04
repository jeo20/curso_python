class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print('estudiando...')
        
nombre = input('Ingrese el nombre: ')
edad = input('Ingrese la edad: ')
grado = input('Ingrese el grado: ')

estudiante = Estudiante(nombre, edad, grado)

print(f"El estudiante se llama {estudiante.nombre}")

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()

