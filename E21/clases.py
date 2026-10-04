#Clases

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio_nuevo):
        if precio_nuevo <= 0:
            print("Ingresa un precio mayor a 0. Intentalo de nuevo")
            return
        self._precio = precio_nuevo
        print(f"Se ha cambiado exitosamente el precio a {self._precio}")
        return
