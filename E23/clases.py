from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """"Clase abstracta Vehiculo para poder crear subclases de tipos de vehículos, esta superclase solo tiene atributos básicos y fundamentales como placa, kilometraje y costo_base_mantenimiento"""
    def __init__(self, placa : str, kilometraje : float, costo_base_mantenimiento : float):
        self.placa = placa
        self.kilometraje = kilometraje
        self.costo_base_mantenimiento = costo_base_mantenimiento

    """Método abstracto para calcular el impuesto de las subclases de tipos de vehículos"""
    @abstractmethod
    def calcular_impuesto(self) -> float:
        return 0.0

    """Método que permite actualizar el kilometraje de cualquier tipo de vehículo, utilizado comúnmente en las clases hijas de tipos de vehículos"""
    def actualizar_kilometraje(self, nuevos_km : float) -> float:
        if nuevos_km <= self.kilometraje:
            print(f"Ingresa una cantidad de kilometros mayor a la actual: {self.kilometraje}")
            return
        self.kilometraje = nuevos_km
        print(f"Se ha actualizado el kilometraje a: {self.kilometraje}")
        return

class Auto(Vehiculo):
    def __init__(self, placa : str, kilometraje : float, costo_base_mantenimiento : float, es_electrico : bool):
        super().__init__(placa, kilometraje, costo_base_mantenimiento)
        self.es_electrico = es_electrico

    def calcular_impuesto(self) -> float:
        """Método heredado de la clase abstracta que retorna el impuesto de los objetos de la clase Auto"""
        if self.es_electrico:
            return 0.0
        return 0.05 * self.kilometraje

class Camion(Vehiculo):
    def __init__(self, placa : str, kilometraje : float, costo_base_mantenimiento : float, ejes : int):
        super().__init__(placa, kilometraje, costo_base_mantenimiento)
        self.ejes = ejes

    def calcular_impuesto(self) -> float:
        """Método heredado de la clase abstracta que retorna el impuesto de los objetos de la clase Camion"""
        return (0.10 * self.kilometraje) + (50.0 * self.ejes) 

class Moto(Vehiculo):
    def __init__(self, placa : str, kilometraje : float, costo_base_mantenimiento : float, cilindrada : float):
        super().__init__(placa, kilometraje, costo_base_mantenimiento)
        self.cilindrada = cilindrada