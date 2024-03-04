# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person:
    # def __init__(self) constructor de una clase
    def __init__(self, name, surname, alias="Sin alias"): # __init__  se usa para crear el constructor de la clase, self es el
                                                         # primer parametro obligatorio, se usa para hacer referencia al objeto
                                                         # que se esta utilizando cuando se llama al metodo
                                                         # se refiere a la misma clase o instancia Person
        # PROPIEDADES DE LA CLASE PERSON: full_name y __name                                                
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self): # metodo get_name, debe tener self como parametro para poder acceder a las propiedades del constructor
        return self.__name

    def walk(self): # metodo walk, debe tener self como parametro para poder acceder a las propiedades del constructor
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure") # le paso 2 parametros a la clase Person
print(my_person.full_name) # imprimo la propiedad full_name de la clase Person
print(my_person.get_name()) 
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)