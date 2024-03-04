class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otropj):
        nuevo_nombre = self.nombre + "-" + otropj.nombre
        nueva_fuerza = round(((self.fuerza + otropj.fuerza)/2)**1.5)
        nueva_velocidad = round(((self.velocidad + otropj.velocidad)/2)**1.5)
        return Personaje(nuevo_nombre,nueva_fuerza, nueva_velocidad) 
            
goku = Personaje("Goku",100,100)
vegeta =  Personaje("Vegeta",99,99)
jiren = Personaje("Jiren",130,140)
gogeta = goku + vegeta
jireta = gogeta + jiren
print(jireta)