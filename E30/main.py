
from typing import Protocol
from dataclasses import dataclass, FrozenInstanceError
import json

# Clases

@dataclass(frozen=True)
class ItemInventario:
    """Clase orientada a datos utilizando el decorador @dataclass"""
    codigo: str
    nombre: str
    precio: float

class Exportable(Protocol):
    """Clase base para el duck typing de elementos exportables, todos los elementos que tengan un comportamiento equivalente al de esta clase serán exportables a JSON"""
    def exportar_json(self) -> str:
        pass

class ReporteInventario:
    """Clase donde se emite el reporte del inventario actual, es equivalente por duck typing a Exportable"""
    def __init__(self, items: list[ItemInventario]):
        self.items = items

    def exportar_json(self) -> str:
        dict_json = {}
        # dict_json = {codigo: {nombre: precio}}
        for producto in self.items:
            dict_json[producto.codigo] = {}
            dict_json[producto.codigo][producto.nombre] = producto.precio
        return json.dumps(dict_json)

def procesar_exportacion(recurso: Exportable) -> None:
    """Función que imprime lo que se va a exportar al archivo JSON, es la que se encarga de ejecutar el duck typing de Expotable"""
    print(recurso.exportar_json())
    return

# Flujo del programa

# Prueba 1
# Esta prueba consiste en verificar que no se puede modificar una dataclass configurada con frozen=True, pues es inmutable lo que lanza el error FrozenInstanceError
try:
    item = ItemInventario("1", "Leche", 15.0)
    item.precio = 0.0
except FrozenInstanceError:
    print("[ERROR]: No se puede cambiar el precio de un producto")

# Prueba 2
# Esta prueba verifica que el duck typing de Exportable funcione correctamente, lo que permite que las clases equivalentes a Exportable pueden pasar por la función procesar_exportacion
item_2 = ItemInventario("2", "Carne", 100.0)
item_3 = ItemInventario("3", "Galletas", 10.0)
inventario_1 = [item_2, item_3]
reporte = ReporteInventario(inventario_1)
procesar_exportacion(reporte)