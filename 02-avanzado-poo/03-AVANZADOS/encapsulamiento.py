"""
El encapsulamiento es un pilar fundamental de la programación orientada a objetos (POO) 
que se refiere a la ocultación de los detalles internos de un objeto y la exposición de una interfaz pública para interactuar con él. 
En Python, el encapsulamiento no es tan estricto como en otros lenguajes, pero se puede implementar de forma efectiva utilizando algunas técnicas.
"""
class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor de atributo privado" #  Atributo privado, solo puede ser accedido desde dentro de la clase.
        self.__atributo_muy_privado = "Esto es muy privado" #  Atributo con visibilidad restringida al interior de la clase
    def __hablar(self):
        print("Hola, como estas")
        
objeto = MiClase()
print(objeto._atributo_privado)    
#print(objeto._atributo_muy_privado) # Error al invocar a atributo_muy_privado
#print(objeto.__hablar) # Error porque el metodo es privado