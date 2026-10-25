"""Clases de modelos.py"""

from abc import ABC, abstractmethod
from estrategias import EstrategiaComision
from excepciones import OperacionInvalidaError

class ActivoFinanciero(ABC):
    """Clase abstracta que permite implementar tres tipos de activos financieros: Accion, Criptomoneda y Bono"""
    def __init__(self, simbolo: str, nombre: str, precio_actual: float, cantidad: float, estrategia_comision: EstrategiaComision):
        self._simbolo = simbolo
        self._nombre = nombre
        self._precio_actual = precio_actual
        self._cantidad = cantidad
        self._estrategia_comision = estrategia_comision

    @property
    def simbolo(self) -> str:
        """Getter del atributo protegido simbolo"""
        return self._simbolo

    @property
    def precio_actual(self) -> float:
        """Getter del atributo protegido precio_actual"""
        return self._precio_actual

    @precio_actual.setter
    def precio_actual(self, nuevo_precio: float) -> None:
        """Setter del atributo protegido precio_actual: Valida si al modificar el precio este es positivo."""
        if nuevo_precio <= 0:
            raise OperacionInvalidaError
        self._precio_actual = nuevo_precio
        return
        
    @property
    def cantidad(self) -> float:
        """Getter del atributo protegido cantidad"""
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad: float) -> None:
        """Setter del atributo protegido cantidad: Valida si al modificar la cantidad ésta es positiva."""
        if nueva_cantidad <= 0:
            raise OperacionInvalidaError
        self._cantidad = nueva_cantidad
        return

    @abstractmethod
    def calcular_valor_total(self) -> float:
        """Método abstracto que obliga a usarse en las implementaciones: Accion, Criptomoneda y Bono"""
        pass

    @abstractmethod
    def evaluar_riesgo(self) -> str:
        """Método abstracto que obliga a usarse en las implementaciones: Accion, Criptomoneda y Bono"""
        pass

    @abstractmethod
    def calcular_valor(self) -> float:
        """Método abstracto que obliga a usarse en las implementaciones: Accion, Criptomoneda y Bono"""
        pass

    def __repr__(self) -> str:
        """Método nativo que da información técnica del objeto"""
        return f"Activo(Simbolo = \'{self._simbolo}\', Cantidad = {self._cantidad})"

    def __eq__(self, otro: object) -> bool:
        """Método nativo que permite definir igualdades entre objetos, distintas a la nativa que compara la id en memoria"""
        if not isinstance(otro, ActivoFinanciero):
            raise OperacionInvalidaError
        simbolo_1 = self._simbolo
        simbolo_2 = otro.simbolo
        if simbolo_1.lower() != simbolo_2. lower():
            pass
        return True

    def __str__(self) -> str:
        return "Activo"

class Accion(ActivoFinanciero):
    "Clase de los objetos acción, calcula el valor total de ellos y retorna su riesgo"
    def __init__(self, simbolo: str, nombre: str, precio_actual: float, cantidad: float, estrategia_comision: EstrategiaComision, sector: str):
        super().__init__(simbolo, nombre, precio_actual, cantidad, estrategia_comision)
        self._sector = sector

    def calcular_valor_total(self) -> float:
        return (self._cantidad*self._precio_actual)+self._estrategia_comision.calcular_comision(self._cantidad*self._precio_actual)
    
    def evaluar_riesgo(self) -> str:
        return "Riesgo Moderado"
    
    def calcular_valor(self, cantidad: float) -> float:
        return (cantidad*self._precio_actual)+self._estrategia_comision.calcular_comision(cantidad*self._precio_actual)

    def __str__(self):
        return f"ID: {self._simbolo} | Empresa: {self._nombre} | Precio Unitario: {self._precio_actual} | Cantidad: {self._cantidad} | Sector: {self._sector}"

class Criptomoneda(ActivoFinanciero):
    "Clase de los objetos criptomoneda, calcula el valor total de ellos y retorna su riesgo"
    def __init__(self, simbolo: str, nombre: str, precio_actual: float, cantidad: float, estrategia_comision: EstrategiaComision, volatilidad: float):
        super().__init__(simbolo, nombre, precio_actual, cantidad, estrategia_comision)
        self._volatilidad = volatilidad

    def calcular_valor_total(self) -> float:
        return (self._cantidad*self._precio_actual)+self._estrategia_comision.calcular_comision(self._cantidad*self._precio_actual)
    
    def evaluar_riesgo(self) -> str:
        if self._volatilidad > 0.5:
            return "Riesgo Alto"
        return "Riesgo Moderado"

    def calcular_valor(self, cantidad: float) -> float:
        return (cantidad*self._precio_actual)+self._estrategia_comision.calcular_comision(cantidad*self._precio_actual)

    def __str__(self):
        return f"ID: {self._simbolo} | Nombre: {self._nombre} | Precio Unitario: {self._precio_actual} | Cantidad: {self._cantidad} | Volatilidad: {self._volatilidad}"

class Bono(ActivoFinanciero):
    "Clase de los objetos Bono, calcula el valor total de ellos y retorna su riesgo"
    def __init__(self, simbolo: str, nombre: str, precio_actual: float, cantidad: float, estrategia_comision: EstrategiaComision, tasa_interes: float):
        super().__init__(simbolo, nombre, precio_actual, cantidad, estrategia_comision)
        self._tasa_interes = tasa_interes

    def calcular_valor_total(self) -> float:
        return self._cantidad*self._precio_actual*(1+self._tasa_interes)+self._estrategia_comision.calcular_comision(self._cantidad*self._precio_actual*(1+self._tasa_interes))
    
    def evaluar_riesgo(self) -> str:
        return "Riesgo Bajo"

    def calcular_valor(self, cantidad: float) -> float:
        return cantidad*self._precio_actual*(1+self._tasa_interes)+self._estrategia_comision.calcular_comision(cantidad*self._precio_actual*(1+self._tasa_interes))
    
    def __str__(self):
        return f"ID: {self._simbolo} | Empresa: {self._nombre} | Precio Unitario: {self._precio_actual} | Cantidad: {self._cantidad} | Tasa de interés: {self._tasa_interes}"