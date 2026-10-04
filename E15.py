#Funciones

def reservar_habitacion(hotel, piso, numero):
    if piso not in hotel:
        print("No tenemos ese piso en este hotel")
        return
    if numero not in hotel[piso]:
        print(f"No tenemos una habitación {numero} en {piso}")
        return

    if hotel[piso][numero]["ocupada"]:
        print(f"La habitación {numero} del {piso} está ocupada")
        return

    hotel[piso][numero]["ocupada"] = True
    tipo = hotel[piso][numero]["tipo"]
    precio = hotel[piso][numero]["precio"]
    print(f"La habitación {numero} del {piso} de tipo: {tipo}, ha sido reservada exitosamente por un precio de: {precio}")
    return

def liberar_habitacion(hotel, piso, numero):
    if piso not in hotel:
        print("No tenemos ese piso en este hotel")
        return
    if numero not in hotel[piso]:
        print(f"No tenemos una habitación {numero} en {piso}")
        return
    
    if not hotel[piso][numero]["ocupada"]:
        print(f"La habitación {numero} del {piso} no está ocupada")
        return
    
    hotel[piso][numero]["ocupada"] = False
    print(f"La habitación {numero} del {piso} fue liberada exitosamente")
    return

def mostrar_habitaciones(hotel):
    for piso in hotel:
        for numero in hotel[piso]:
            tipo = hotel[piso][numero]["tipo"]
            precio = hotel[piso][numero]["precio"]
            estado = hotel[piso][numero]["ocupada"]
            if estado:
                print(f"{piso}| Habitación {numero}, Tipo : {tipo}, Precio : {precio}, Estado: Ocupada")
            else:
                print(f"{piso}| Habitación {numero}, Tipo : {tipo}, Precio : {precio}, Estado: Disponible")
    return

#Estructuras de datos

hotel = {
    "Piso 1": {
        "101": {"tipo": "Individual", "precio": 50.0, "ocupada": False},
        "102": {"tipo": "Doble", "precio": 80.0, "ocupada": True}
    },
    "Piso 2": {
        "201": {"tipo": "Suite", "precio": 150.0, "ocupada": False}
    }
}

#Menú general del programa

abierto = True
opcion = 0
while abierto:
    print("Sistema de Gestión de Reservas de Hotel")
    print("1. Reservar habitación")
    print("2. Liberar habitación")
    print("3. Mostrar habitaciones")
    print("4. Salir")
    opcion = int(input("¿Cual opción vas a elegir? "))
    print(" ")
    if opcion == 1:
        piso = input("¿Cuál es el piso en el que se encuentra la habitación? ")
        numero = input("¿Cuál es el número de la habitación? ")
        reservar_habitacion(hotel, piso, numero)
        print(" ")
    elif opcion == 2:
        piso = input("¿Cuál es el piso en el que se encuentra la habitación? ")
        numero = input("¿Cuál es el número de la habitación? ")
        liberar_habitacion(hotel, piso, numero)
        print(" ")
    elif opcion == 3:
        mostrar_habitaciones(hotel)
        print(" ")
    elif opcion ==  4:
        abierto = False
        print("Saliendo...")
    else:
        print("Elige una de las opciones mostradas")
        print(" ")
        opcion = 0