"""Clases de portafolio.py"""

from excepciones import ActivoExistenteError, ActivoNoEncontrado, FondosInsuficientesError, OperacionInvalidaError
from modelos import ActivoFinanciero

class Portafolio:
    "Clase del objeto Portafolio, donde se almacenan los objetos de las subclases de ActivoFinanciero en una lista, y la que realiza las operaciones con ellos"
    def __init__(self, activos: list, saldo_efectivo: float):
        self._activos = activos
        self._saldo_efectivo = saldo_efectivo

    @property
    def saldo_efectivo(self) -> float:
        """Getter del atributo protegido saldo_efectivo"""
        return self._saldo_efectivo
    
    @saldo_efectivo.setter
    def saldo_efectivo(self, saldo_nuevo: float) -> None:
        """Setter del atributo protegido saldo_efectivo"""
        if saldo_nuevo <= 0:
            raise OperacionInvalidaError
        self._saldo_efectivo += saldo_nuevo
        return
        
    def agregar_activo(self, activo: ActivoFinanciero) -> None:
        """Método que permite agregar activos a la estructura de datos dentro de la instancia Portafolio"""
        if not isinstance(activo, ActivoFinanciero):
            raise OperacionInvalidaError
        if activo in self._activos:
            raise ActivoExistenteError(activo.simbolo)
        if self._saldo_efectivo < activo.calcular_valor_total():
            raise FondosInsuficientesError(activo.calcular_valor_total(), self._saldo_efectivo)
        self._saldo_efectivo -= activo.calcular_valor_total()
        self._activos.append(activo)
        return

    def comprar_activo(self, simbolo: str, cantidad_adicional: float) -> None:
        """Método que permite comprar más activos que ya están dentro de la instancia Portafolio"""
        if cantidad_adicional <= 0:
            raise OperacionInvalidaError
        for activo in self._activos:
            if activo.simbolo == simbolo:
                if self._saldo_efectivo < activo.calcular_valor(cantidad_adicional):
                    raise FondosInsuficientesError(activo.calcular_valor(cantidad_adicional), self._saldo_efectivo)
                activo.cantidad += cantidad_adicional
                self._saldo_efectivo -= activo.calcular_valor(cantidad_adicional)
                return
        raise ActivoNoEncontrado(simbolo)

    def calcular_valor_total_portafolio(self) -> float:
        """Método que devuelve todo el valor del Portafolio"""
        valor_total_portafolio = 0
        for activo in self._activos:
            valor_total_portafolio += activo.calcular_valor_total()
        valor_total_portafolio += self._saldo_efectivo
        return valor_total_portafolio

    def __len__(self) -> int:
        """Método nativo que permite usar la función len() en la instancia Portafolio"""
        return len(self._activos)

    def __getitem__(self, posicion: int) -> ActivoFinanciero:
        """Método nativo que permite indexar y convertir en iterable la instancia Portafolio"""
        return self._activos[posicion]