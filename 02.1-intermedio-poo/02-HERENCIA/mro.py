class A:
    def hablar(self):
        print("Hablo desde A")

class B(A):
    def hablar(self):
        print("Hablo desde B")
    
class C(A):
    def hablar(self):
        print("Hablo desde C")
        
class D(B,C):
    def hablar(self):
        print("Hablo desde D")
        
d = D()

d.hablar()  # Hablo desde D

print(D.mro()) # Muestra el Orden de Resolucion de Metodos (MRO) 

B.hablar(d)   # Llamada a método de clase B para ver que pasa si se llama directamente a él