
class InventarioError(Exception):
    """Clase base de errores del Inventario"""
    pass

class StockInsuficienteError(InventarioError):
    def __init__(self, producto: str, stock_actual: int, cantidad_solicitada: int):
        """Error lanzado cuando la cantidad solicitada del producto es mayor a la actual"""
        self.producto = producto
        self.stock_actual = stock_actual
        self.cantidad_solicitada = cantidad_solicitada
        super().__init__(f"Error: Faltan {self.cantidad_solicitada - self.stock_actual} del producto: {self.producto} para realizar la transacción")

class ProductoExistenteError(InventarioError):
    def __init__(self, nombre_producto: str):
        """Error lanzado cuando el producto ya existe en el inventario"""
        self.nombre_producto = nombre_producto
        super().__init__(f"El producto {self.nombre_producto} ya se encuentra en el inventario")

class ProductoInexistenteError(InventarioError):
    def __init__(self, nombre_producto: str):
        """Error lanzado cuando el producto no existe en el inventario"""
        self.nombre_producto = nombre_producto
        super().__init__(f"El producto {self.nombre_producto} no se encuentra en el inventario")

class Inventario:
    """Clase del objeto Inventario que gestiona los productos que hay y sus ventas"""
    def __init__(self, productos: dict):
        # productos = {producto, cantidad_producto}
        self._productos = productos

    @property
    def productos(self) -> dict:
        return self._productos

    @productos.setter
    def productos(self, producto: str, cantidad_producto: int) -> None:
        self._productos[producto] = cantidad_producto
        return

    def agregar_producto(self, producto: str, cantidad_producto: int) -> None:
        if producto in self.productos:
            raise ProductoExistenteError(producto)
        if cantidad_producto <= 0:
            raise "Error: La cantidad del producto a agregar tiene que ser mayor a 0"
        self.productos[producto] = cantidad_producto
        print(f"Se ha agregado {cantidad_producto} de {producto}. Stock: {self.productos[producto]}")
        return

    def vender_producto(self, producto: str, cantidad_solicitada: int) -> None:
        if producto not in self.productos:
            raise ProductoInexistenteError(producto)
        if cantidad_solicitada > self.productos[producto]:
            raise StockInsuficienteError(producto, self.productos[producto], cantidad_solicitada)
        self.productos[producto] -= cantidad_solicitada
        print(f"Se ha vendido {cantidad_solicitada} de {producto}. Stock: {self.productos[producto]}")
        return 

inventario1 = Inventario({})
inventario1.agregar_producto("Manzana", 10)
inventario1.agregar_producto("Manzana", 20)
# Capturamos el error ProductoExistenteError 
inventario1.vender_producto("Manzana", 100)
# Capturamos el error StockInsuficienteError