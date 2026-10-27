# Ejercicio de calentamiento de creación de dataclasses y duck typing con protocols (E30)

Requerimientos del código:
Estructura de Datos con @dataclass:

Importa dataclass y FrozenInstanceError desde dataclasses.

Define la dataclass ItemInventario configurada con frozen=True.

Atributos: codigo: str, nombre: str, precio: float.

Interfaz Estructural con Protocol:

Importa Protocol desde typing.

Define el Protocol llamado Exportable con el método exportar_json(self) -> str: ....

Clase Concreta:

Crea la clase ReporteInventario.

Recibe en su __init__ una lista de objetos ItemInventario (items: list[ItemInventario]).

Importante: NO debe heredar de Exportable.

Implementa el método exportar_json(self) -> str para devolver una representación formateada en texto (JSON simulado) de los elementos de su lista.

Función de Procesamiento:

Define la función procesar_exportacion(recurso: Exportable) -> None que ejecute e imprima recurso.exportar_json().

Flujo de Prueba en main.py (Especificación explicita de bloques de control):

Prueba 1 (Inmutabilidad):

Instancia un ItemInventario.

Instrucción de control de error: Escribe un bloque try / except FrozenInstanceError por FUERA de la línea donde intentes modificar item.precio = 50.0 para capturar la excepción y confirmar la inmutabilidad en la consola.

Prueba 2 (Duck Typing con Protocol):

Crea dos ítems de inventario, pásalos dentro de una lista a una instancia de ReporteInventario, y envía ese reporte a la función procesar_exportacion() para verificar que funciona sin herencia explícita.

## 📁 Estructura del Proyecto
├── main.py Código fuente donde se ejecuta el ejercicio.


DUDAS: 

Errores: 