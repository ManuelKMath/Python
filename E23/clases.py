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