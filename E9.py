def agregar_producto(inventario):
	nombre_producto = input("¿Cual es el nombre del producto? ")
	precio_producto = float(input("¿Cuanto vale el producto? "))
	cantidad_producto = int(input("¿Cual es la cantidad? "))
	inventario[nombre_producto] = {"precio" : precio_producto, "cantidad" : cantidad_producto}
	
	return inventario
	
def mostrar_inventario(inventario):
	if inventario == {}:
		print("El inventario esta vacio.")
		
	else:
		for nombre_producto, precio_y_cantidad_keys in inventario.items():
					precio_y_cantidad = list(precio_y_cantidad_keys.values())
					print(f"Producto: {nombre_producto} Precio: {precio_y_cantidad[0]} Cantidad: {precio_y_cantidad[1]} ")
					
	return 
	
def buscar_producto(inventario):
	producto_buscado = input("¿Cual es el producto que buscas?")
	contador = 1
	for producto_actual, precio_y_cantidad_keys in inventario.items():
		if producto_actual == producto_buscado:
					precio_y_cantidad = list(precio_y_cantidad_keys.values())
					print(f"Si hay {producto_actual}, tenemos {precio_y_cantidad[1]} y su precio es {precio_y_cantidad[0]}")
					contador = 0
					break
		else:
			pass
	
	if contador > 0:
		print("No tenemos ese producto")
		
	return
	
def calcular_valor_total(inventario):
	valor_total_inventario = 0
	for nombre_producto, precio_y_cantidad_keys in inventario.items():
					precio_y_cantidad = list(precio_y_cantidad_keys.values())
					precio_total_producto = precio_y_cantidad[0] * precio_y_cantidad[1]
					valor_total_inventario += precio_total_producto
					
	return valor_total_inventario

abierto = True
opcion = 0
inventario = {}
while abierto:
	if opcion == 0:
		print("Gestor de Inventario")
		print("1. Agregar o actualizar un producto")
		print("2. Ver el inventario completo")
		print("3. Buscar un producto por nombre")
		print("4. Calcular el valor total del inventario")
		print("5. Salir del programa")
		opcion = int(input("Ingresa la opcion que vas a elegir: "))
	elif opcion == 1:
		inventario = agregar_producto(inventario)
		opcion = 0
	elif opcion == 2:
		mostrar_inventario(inventario)
		opcion = 0
	elif opcion == 3:
		buscar_producto(inventario)
		opcion = 0
	elif opcion == 4:
		print(calcular_valor_total(inventario))
		opcion = 0
	elif  opcion == 5:
		print("Saliendo...")
		abierto = False
	else:
		opcion = 0
		





