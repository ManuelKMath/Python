"""Clases de estrategias.py"""

from abc import ABC, abstractmethod

class EstrategiaComision(ABC):
    """Clase abstracta que permite implementar dos tipos de comisiones distintas, una fija y una porcentual"""
    @abstractmethod
    def calcular_comision(self, monto: float) -> float:
        """Método abstracto que obliga a usarse en las implementaciones: ComisionFija y ComisionPorcentual"""
        pass

class ComisionFija(EstrategiaComision):
    def calcular_comision(self, monto: float) -> float:
        """Método heredado de EstrategiaComision y sobreescrito para devolver un valor fijo"""
        return 5.0

class ComisionPorcentual(EstrategiaComision):
    def calcular_comision(self, monto: float) -> float:
        """Método heredado de EstrategiaComision y sobreescrito para devolver un valor porcentual"""
        comision = monto * 0.015
        if comision <= 2.0:
            return 2.0
        return comision