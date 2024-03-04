"""
La abstracción es un concepto fundamental en la programación orientada a objetos (POO) que se refiere
a la capacidad de ocultar los detalles de implementación de un objeto y enfocarse en su comportamiento.
En Python, la abstracción se puede lograr mediante el uso de clases, métodos y herencia.
"""
class Auto():
    def __init__(self):
        self._estado = "apagado"
        
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
        
    def conducir(self):
        if self._estado == "apagado": #  Abstraccion: solo se puede conducir si el auto está encendido
            self.encender() # llamamos al metodo encender para encender el auto antes de conducir
        print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir( )  # El auto no esta encendido, primero debemos encenderlo