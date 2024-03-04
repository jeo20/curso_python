"""
El decorador @property en Python es una herramienta que se utiliza para convertir un método en un atributo de solo lectura.
Esto significa que el método se puede llamar como si fuera un atributo normal, pero no se puede modificar su valor.
"""
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter # Esto es un decorador de la propiedad "nombre". Se utiliza para hacer que el atributo sea privado y solo se pueda acceder a través del getter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter # Eliminar el atributo nombre
    def nombre(self):
        del self.__nombre
        
jeo = Persona("Jorge", 45)

nombre = jeo.nombre 

print(nombre)

#### MODIFICO NOMBRE    
jeo.nombre = "Otro nombre"

nombre = jeo.nombre 

print(nombre)

##### ELIMINO NOMBRE
del jeo.nombre

print(nombre)
    