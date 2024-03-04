"""
Getters y setters son métodos especiales que se utilizan para obtener y establecer valores de atributos de una clase en Python.
Aunque no son obligatorios, su uso se recomienda para encapsular la lógica de acceso y modificación de los atributos,
mejorando la seguridad, modularidad y flexibilidad del código.

¿Qué son los getters?
Los getters son métodos que recuperan el valor de un atributo de la clase. 
Se definen utilizando el decorador @property. 
El nombre del método suele ser el mismo que el del atributo que se desea obtener.

¿Qué son los setters?

Los setters son métodos que establecen el valor de un atributo de la clase. 
Se definen utilizando el decorador @nombre.setter. 
El nombre del método suele ser el mismo que el del atributo que se desea modificar.

"""
class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self,new_nombre):
        self._nombre = new_nombre
    
    
jeo = Persona("Jorge", 45)
nombre = jeo.get_nombre() #  llamada al getter para acceder a _nombre
print(nombre)
    
jeo.set_nombre("Eduardo") #  llamada al setter para cambiar _nombre

nombre = jeo.get_nombre() #  llamada al getter nuevamente para comprobar si ha sido actualizado</s
print(nombre)
