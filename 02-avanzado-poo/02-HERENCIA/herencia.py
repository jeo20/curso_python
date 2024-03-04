"""
La herencia permite que se puedan definir nuevas clases basadas de unas ya existentes a fin de reutilizar el código, 
generando así una jerarquía de clases dentro de una aplicación. 
Si una clase deriva de otra, esta hereda sus atributos y métodos y puede añadir nuevos atributos, métodos o redefinir los heredados.
"""
class Persona: #Clase base o padre, es la clase principal que todos los demás heredan
    def __init__(self, nombre, edad, nacionalidad): # constructor para inicializar los atributos (nombre, edad, nacionalidad) de la clase Persona
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola estoy hablando")
        
class Empleado(Persona): #Empleado hereda de la clase Persona , es una clase hija o derivada
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super ().__init__(nombre, edad, nacionalidad) #Se llama al constructor de la clase padre(Persona) para inicializar las variables comunes a ambas
        self.trabajo = trabajo
        self.salario = salario

    def hablar(self):
        print("No") #Sobreescribiendo el método hablar de la clase padre(Persona)

class Estudiante(Persona): #Estudiante hereda de la clase Persona , es una clase hija o derivada
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super ().__init__(nombre, edad, nacionalidad) #Se llama al constructor de la clase padre(Persona) para inicializar las variables comunes a ambas
        self.notas = notas
        self.universidad = universidad
        

jorge = Empleado("Jorge", 45, "Argentino", "Desarrollador", 1000)

print(jorge.nombre)