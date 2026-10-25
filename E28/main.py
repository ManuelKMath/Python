# Main.py

from functools import wraps

# Flujo del programa

if __name__ == "__main__":

    def auditar_ejecucion(func):
        """Decorador que registra cuándo se utiliza la función dividir y cuándo falla o cuándo se ejecuta exitosamente"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG]: Ejecutando {func.__name__} con args: a: float y b: float y kwargs: ")
            try:
                resultado = func(*args, **kwargs)
            except ZeroDivisionError:
                print(f"[LOG ALERTA]: {func.__name__} falló con la excepción: ZeroDivisionError")
                raise ZeroDivisionError
            print(f"[LOG]: {func.__name__} finalizó correctamente. Resultado: {resultado}")
            return resultado 
        return wrapper

    @auditar_ejecucion
    def dividir(a: float, b: float) -> float:
        """Función que divide dos números"""
        if b == 0:
            raise ZeroDivisionError
        return a / b

    try:
        print(dividir(10, 2))
        print(dividir(10, 0))
    except ZeroDivisionError:
        print("[ERROR] División por cero. Intentélo de nuevo")
