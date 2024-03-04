"""
Una clase abstracta en Python es una plantilla para una clase que define una estructura y comportamiento común para 
un conjunto de clases relacionadas. 
No se puede instanciar directamente, es decir, no se pueden crear objetos directamente a partir de ella.
Su propósito es servir como base para crear clases derivadas o subclases que hereden sus características y
las completen con implementaciones específicas.
"""
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad  
        self.sexo = sexo 
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self): #Método Abstracto trabajar
        pass
    # Clase hija (subclase) de la clase "Persona".
    
    def presentarse(self):
        print (f"Hola me llamo {self.nombre} y mi edad es: {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}")
            
            
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy trabajando en: {self.actividad}")   
                 
# Error porque quiere instanciar desde una clase abstracta    
jeo_estudiante = Estudiante("Jorge",30,"M","Programacion") 
jeo_estudiante.hacer_actividad()

jeo_trabajador = Trabajador("Eduardo",45,"M","Liquidacion de Sueldos") 
jeo_trabajador.presentarse()
jeo_trabajador.hacer_actividad()