
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

    @property
    def costo_base_mantenimiento(self):
        return self._costo_base_mantenimiento

    @costo_base_mantenimiento.setter
    def costo_base_mantenimiento(self, nuevo_costo_base_mantenimiento : float):
        if nuevo_costo_base_mantenimiento <= 0:
            print("Introduce un nuevo costo base del mantenimiento mayor a 0")
            return
        self._costo_base_mantenimiento = nuevo_costo_base_mantenimiento
        print(f"Se ha cambiado exitosamente el costo base del mantenimiento a {self._costo_base_mantenimiento}")
        return

    def calcular_mantenimiento(self):
        return self.costo_base_mantenimiento

    @property
    def placa(self):
        return self._placa

    def __str__(self):
        return f"Placa: {self._placa} Marca: {self._marca} Kilometraje: {self._kilometraje} Costo base mantenimiento: {self._costo_base_mantenimiento}"

class Camion(Vehiculo):
    def __init__(self, placa, marca, kilometraje : float, costo_base_mantenimiento : float, capacidad_toneladas : float):
        super().__init__(placa, marca, kilometraje, costo_base_mantenimiento)
        self._capacidad_toneladas = capacidad_toneladas

    def calcular_mantenimiento(self):
        return self.costo_base_mantenimiento + (0.15 * self._capacidad_toneladas)

    def __str__(self):
        return  f"Placa: {self._placa} Marca: {self._marca} Kilometraje: {self._kilometraje} Costo base mantenimiento: {self._costo_base_mantenimiento} Capacidad de toneladas: {self._capacidad_toneladas}"

class Furgoneta(Vehiculo):
    def __init__(self, placa, marca, kilometraje : float, costo_base_mantenimiento : float, es_refrigerada : bool):
        super().__init__(placa, marca, kilometraje, costo_base_mantenimiento)
        self._es_refrigerada = es_refrigerada

    def calcular_mantenimiento(self):
        if self._es_refrigerada:
            return self.costo_base_mantenimiento + 200.0
        else:
            return self.costo_base_mantenimiento
