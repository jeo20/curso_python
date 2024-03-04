"""
El polimorfismo es la capacidad de que diferentes objetos respondan al mismo mensaje de diferentes maneras. 
En otras palabras, dos objetos de diferentes clases pueden tener métodos con el mismo nombre, 
y ambos métodos pueden ser llamados con el mismo código, pero con diferentes comportamientos.
"""
class Perro():
    def sonido(self):
        return("Guau!") # Retorna Guau

class Gato():
    def sonido(self):
        return("Miau!") # Retorna Miau

def hacer_sonido(animal): # Aquí se utiliza Polimorfismo para que un solo método pueda ser llamado en diferentes animales
    print(animal.sonido())

perro = Perro()
gato = Gato()

#hacer_sonido(perro) # Imprime "Guau!"
print(perro.sonido()) #  Imprime "Guau!"

# hacer_hablar(gato) # Imprime "Miau!"
# #print(gato.hablar()) #  Imprime "Miau!"
