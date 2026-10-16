from abc import ABC, abstractmethod

class ServicioNotificacion(ABC):
    """Clase abstracta que se encarga de ser la base para el método abstracto enviar_mennsaje"""
    @abstractmethod
    def enviar_mensaje(self, destinatario : str, mensaje : str) -> None:
        pass

class NotificadorEmail(ServicioNotificacion):
    """Subclase de ServicioNotificacion que imprime un mensaje específico si es un email"""
    def enviar_mensaje(self, destinatario : str, mensaje: str) -> None:
        print(f"Enviando EMAIL a [{destinatario}]: {mensaje}")
        return

class NotificadorSMS(ServicioNotificacion):
    """Subclase de ServicioNotificacion que imprime un mensaje específico si es un SMS"""
    def enviar_mensaje(self, destinatario, mensaje) -> None:
        print(f"Enviando SMS a [{destinatario}]: {mensaje}")
        return

class SistemaAlerta:
    """Clase que llama al objeto de la clase ServicioNotificacion para imprimer un mensaje"""
    def __init__(self, servicio_notificacion : ServicioNotificacion):
        self._servicio_notificacion = servicio_notificacion

    def notificar_usuario(self, usuario: str, alerta: str) -> None:
        self._servicio_notificacion.enviar_mensaje(usuario, alerta)
        return

#Ejercicio de prueba de la práctica de composición de objetos sobre herencia, aquí se crean dos objetos con componentes distintos y se verifica que cada lógica funcione de manera distinta

email = NotificadorEmail()
sms = NotificadorSMS()

sistema1 = SistemaAlerta(email)
sistema2 = SistemaAlerta(sms)

sistema1.notificar_usuario("User", "Mensaje1")
sistema2.notificar_usuario("User", "Mensaje2")
