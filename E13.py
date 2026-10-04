
#Funciones

def procesar_compra(catalogo):
    producto = input("¿Cuál es el producto que desea comprar? ")
    categoria = input("¿Cuál es la categoria del producto? ")
    cantidad = int(input("¿Cuántos quieres comprar? "))

    if categoria in catalogo:
        if producto in catalogo[categoria]:
            if cantidad > 0:
                if  catalogo[categoria][producto]["stock"] > 0:
                    if cantidad <= catalogo[categoria][producto]["stock"]:
                        catalogo[categoria][producto]["stock"] = catalogo[categoria][producto]["stock"] - cantidad
                        precio_total =  catalogo[categoria][producto]["precio"] * cantidad
                        print(f"La compra de {cantidad} {producto} de la categoria {categoria} por un precio unitario de {catalogo[categoria][producto]["precio"]} y un precio total de {precio_total} fue realizada exitosamente.")
                    else:
                        print(f"La cantidad que deseas comprar debe ser mayor que 0 y menor o igual que {catalogo[categoria][producto]["stock"]}")
                else:
                    print("No tenemos stock de ese producto ahora mismo")
            else:
                print(f"La cantidad que deseas comprar debe ser mayor que 0 y menor o igual que {catalogo[categoria][producto]["stock"]}")
        else:
            print(f"No tenemos ese producto en la categoria {categoria}")
    else: 
        print("No tenemos esa categoria en nuestro catalogo")
    return

def consultar_precio(catalogo, producto, categoria):
    if categoria in catalogo:
        if producto in catalogo[categoria]:
            print(f"El precio de {producto} de la categoria {categoria} tiene un precio unitario de {catalogo[categoria][producto]["precio"]}")
        else:
            print(f"El producto no está en la categoria {categoria}")
    else:
        print("No tenemos esa categoria en nuestro catalogo")
    return

def consultar_stock(catalogo, producto, categoria):
    if categoria in catalogo:
        if producto in catalogo[categoria]:
             print(f"El precio de {producto} de la categoria {categoria} tiene un stock de {catalogo[categoria][producto]["stock"]}")
        else:
            print(f"El producto no está en la categoria {categoria}")
    else:
        print("No tenemos esa categoria en nuestro catalogo")
    return

def consultar_precio_y_stock(catalogo, producto, categoria):
    consultar_precio(catalogo, producto, categoria)
    consultar_stock(catalogo, producto, categoria)
    return
    
#Estructuras de datos

catalogo = {"Laptops": {"HP ProBook": {"precio": 450.0, "stock": 10}, "Lenovo ThinkPad": {"precio": 600.0, "stock": 5}},"Accesorios": {"Mouse Logi": {"precio": 25.0, "stock": 15}}}

#Menú del programa

abierto = True
opcion = 0
while abierto:
    print("Procesador de Pedidos y Stock")
    print("1. Procesar compra")
    print("2. Consultar precio y stock")
    print("3. Salir")
    opcion = int(input("¿Cual opción vas a elegir? "))
    print(" ")
    if opcion == 1:
        procesar_compra(catalogo)
        print(" ")
    elif opcion == 2:
        producto = input("¿Cuál es el producto al que le desea consultar el precio? ")
        categoria = input("¿Cuál es la categoria del producto? ")
        consultar_precio_y_stock(catalogo, producto, categoria)
        print(" ")
    elif opcion ==  3:
        abierto = False
        print("Saliendo...")
    else:
        print("Elige una de las opciones mostradas")
        print(" ")
        opcion = 0