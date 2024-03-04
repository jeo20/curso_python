"""
LSP (Principio de sustitución de Liskov): 
Los objetos de una clase deben poder ser reemplazados por objetos de sus subclases sin alterar 
el comportamiento correcto del programa.
"""
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        print("Estoy Volando")

class AveNoVoladora(Ave):
    pass
