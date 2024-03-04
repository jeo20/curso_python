"""
ISP (Principio de interfaz de segregación): Las interfaces deben ser lo más pequeñas y específicas posible.

En este caso, con interfaz nos referimos a las clases abstractas
"""
from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")

robot = Robot()
robot.trabajar()

humano = Humano()
humano.comer()