
class Vehiculo:
    def __init__(self, placa, marca, kilometraje : float, costo_base_mantenimiento : float):
        self._placa = placa.upper()
        self._marca =  marca
        self._kilometraje = kilometraje
        self._costo_base_mantenimiento = costo_base_mantenimiento

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, kilometraje_nuevo : float):
        if kilometraje_nuevo <= self._kilometraje:
            print(f"Introduce un kilometraje mayor que el actual: {self._kilometraje}")
            return
        self._kilometraje = kilometraje_nuevo
        print(f"Se ha cambiado exitosamente el kilometraje a {self._kilometraje}")
        return 