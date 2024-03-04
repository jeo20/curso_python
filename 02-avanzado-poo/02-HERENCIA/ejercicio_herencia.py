class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super ().__init__(nombre, edad)
        self.grado = grado 
    
    def imprimir_estudiante(self):
        super().imprimir()
        print(f"El grado del estudiante es {self.grado}.")

# Crear una persona
p1 = Persona("Juan", 25)
print("\nInformación de la persona Juan:\n")
p1.imprimir()

# Crear un estudiante
e1 = Estudiante("Ana", 18, "3ro grado")
print("\n\nInformación del estudiante Ana:\n")
e1.imprimir_estudiante()