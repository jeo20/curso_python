########### INICIO CLASE CELULAR #######################
class Celular(): # Definicion clase Celular
    def __init__(self, marca, modelo, camara): #constructor __init__ y definicion de atributos
        self.marca = marca # atributo marca
        self.modelo = modelo # atributo modelo
        self.camara = camara # atributo camara

######### DEFINICION DE METODOS DE LA CLASE CELULAR SIEMPRE LLEVAN EL PARAMETRO SELF        
    def llamar(self): # metodo llamar
        print(f'Estas realizando una llamada desde: {self.modelo}')
        
    def cortar(self): # metodo cortar
        print(f'Cortarste la llamada desde: {self.modelo}')         

########### FIN CLASE CELULAR #######################

#### CREANDO INSTANCIAS ####    
celular1 = Celular("Samsung","S23","48MP") # creando una instancia celular1 de la clase Celular y defino los atributos
celular2 = Celular("Apple","Iphone 15 Pro","56MP") # creando una instancia celular2 de la clase Celular y defino los atributos

### INVOCANDO UN METODO DE LA CLASE CELULAR ###
celular1.llamar() # invoco al metodo llamar de la clase Celular
#  Estas realizando una llamada desde: Samsung S23