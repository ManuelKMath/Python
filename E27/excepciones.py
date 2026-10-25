"""Clases de excepciones.py"""

class FinanzasError(Exception):
    """Clase base de errores"""
    pass

class ActivoExistenteError(FinanzasError):
    """Clase que se encarga del error ActivoExistenteError, este error se lanza cuando ya hay un activo igual en la lista de activos"""
    def __init__(self, simbolo: str):
        self.simbolo = simbolo
        super().__init__(f"[ERROR]: ACTIVO YA EXISTENTE")

class ActivoNoEncontrado(FinanzasError):
    """Clase que se encarga del error ActivoNoEncontrado, este error se lanza cuando no hay un activo igual en la lista de activos"""
    def __init__(self, simbolo: str):
        self.simbolo = simbolo
        super().__init__(f"[ERROR]: ACTIVO NO ENCONTRADO")

class FondosInsuficientesError(FinanzasError):
    """Clase que se encarga del error FondosInsuficientesError, este error se lanza cuando no hay suficiente saldo para concretar una transacción"""
    def __init__(self, monto_requerido : float, saldo_disponible: float):
        self.monto_requerido = monto_requerido
        self.saldo_disponible = saldo_disponible
        super().__init__(f"[ERROR]: FONDOS INSUFICIENTES")

class OperacionInvalidaError(FinanzasError):
    def __init__(self):
        super().__init__("[ERROR]: OPERACIÓN INVALIDA")