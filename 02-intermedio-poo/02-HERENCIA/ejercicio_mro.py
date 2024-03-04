class Animal: # Clase principal, sin constructor porque no hay que inicializar atributos
    def comer(self):
        print("Animal comiendo")
    
class Mamifero(Animal):
    def amamantar(self):
        print("Mamifero amamantando")

class Ave(Animal):
    def volar(self):
        print("Ave volando")
        
class Murcielago(Mamifero,Ave):
    pass
        
murcielago = Murcielago()
murcielago.comer() # Accede al metodo de la clase Animal 
murcielago.amamantar() #  Accede al método de la clase Mamifero
murcielago.volar() # Ejecutará el método de la clase que lo hereda primero (en este caso Ave) y luego el del padre (Mamifero).
