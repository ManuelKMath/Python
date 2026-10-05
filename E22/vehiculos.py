
class Vehiculo:
    def __init__(self, placa, marca, kilometraje : float, costo_base_mantenimiento : float):
        self._placa = placa.upper()
        self._marca =  marca
        self._kilometraje = kilometraje
        self._costo_base_mantenimiento = costo_base_mantenimiento