"""
OCP (Principio abierto-cerrado): Las clases deben estar abiertas para extensión, pero cerradas para modificación.
Se pueden agregar funcionalidades(creando nuevas clases) pero no modifcar la clase padre
"""

class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError # Este metodo debe ser implementado en las clases hijas
        
# Clase para enviar correos electronicos        
class NotificadorEmail(Notificador): # Clase hija de Notificador
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.email}")

#  Clase para enviar SMS
class NotificadorSMS(Notificador): # Clase hija de Notificador
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.sms}")

# Clase para enviar WhatsappS
class NotificadorWhatsApp(Notificador): # Clase hija de Notificador
    def notificar(self):
        print(f"Enviando Whatsapp a {self.usuario.whatsapp}")