#Funciones

def menu(flota):
    while True:
        print("\n---Sistema de Gestión de Alquiler de Vehículos---")
        print("1. Consultar vehículo")
        print("2. Alquilar vehículo")
        print("3. Devolver vehículo")
        print("4. Mostrar flota")
        print("5. Salir")

        try:
            opcion = int(input("Introduce la opción que vas a elegir: "))
        except ValueError:
            print("Tienes que introducir uno de los números de las opciones que aparecen en el menú")
            continue

        match opcion:
            case 1:
                sucursal = input("Introduce la sucursal donde está el vehículo: ")
                id_vehiculo = input("Introduce el ID del vehículo que quieres consultar: ")
                consultar_vehiculo_seguro(flota, sucursal, id_vehiculo)
                print(" ")
            case 2:
                sucursal = input("Introduce la sucursal donde está el vehículo: ")
                id_vehiculo = input("Introduce el ID del vehículo que quieres consultar: ")
                try:
                    dias = int(input("Introduce la cantidad de días que lo vas a alquilar: "))
                except ValueError:
                    print("Introduce un numero mayor que 0 de días")
                    continue
                codigo_promo = input("Introduce el código de promoción (Si tienes uno): ")
                alquilar_vehiculo(flota, sucursal, id_vehiculo, dias, codigo_promo)
                print(" ")
            case 3:
                sucursal = input("Introduce la sucursal de donde alquilaste el vehículo: ")
                id_vehiculo = input("Introduce el ID del vehículo que quieres devolver: ")
                devolver_vehiculo(flota, sucursal, id_vehiculo)
                print(" ")
            case 4:
                mostrar_flota(flota)
                print(" ")
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Elige una de las opciones que aparece en el menú")
                print(" ")
    return

def consultar_vehiculo_seguro(flota, sucursal, id_vehiculo):
    vehiculos_sucursal = flota.get(sucursal)
    if vehiculos_sucursal is None:
        print("Esta sucursal no existe")
        return
    vehiculos_id = vehiculos_sucursal.get(id_vehiculo)
    if vehiculos_id is None:
        print(f"No tenemos un vehículo con la ID ingresada")
        return

    modelo = flota[sucursal][id_vehiculo]["modelo"]
    precio = flota[sucursal][id_vehiculo]["precio_dia"]
    estado = flota[sucursal][id_vehiculo]["alquilado"]
    if estado:
        print(f"Vehículo: {modelo}, Precio: {precio}, Sucursal: {sucursal}, Alquilado")
    else:
        print(f"Vehículo: {modelo}, Precio: {precio}, Sucursal: {sucursal}, Disponible")
    return

def alquilar_vehiculo(flota, sucursal, id_vehiculo, dias, codigo_promo):
    if sucursal not in flota:
        print("No tenemos esa sucursal")
        return
    if id_vehiculo not in flota[sucursal]:
        print(f"No tenemos un vehículo con la ID: {id_vehiculo}")
        return
    if dias <= 0:
        print("Introduce un numero mayor que 0 de días")
        return
    if flota[sucursal][id_vehiculo]["alquilado"]:
        print(f"El vehículo con la ID: {id_vehiculo} ya ha sido alquilado")
        return
    precio_dia = flota[sucursal][id_vehiculo]["precio_dia"]
    modelo = flota[sucursal][id_vehiculo]["modelo"]
    porcentaje_descuento = DESCUENTOS.get(codigo_promo.upper(), 0.0)
    monto_base = precio_dia * dias
    monto_total = monto_base - (monto_base * porcentaje_descuento)
    flota[sucursal][id_vehiculo]["alquilado"] = True
    print(f"Se ha alquilado el vehículo {modelo} con ID: {id_vehiculo} por un monto total de: {monto_total} con un descuento de {porcentaje_descuento * 100} %")
    return

def devolver_vehiculo(flota, sucursal, id_vehiculo):
    vehiculos_sucursal = flota.get(sucursal)
    if vehiculos_sucursal is None:
        print("Esta sucursal no existe")
        return
    vehiculos_id = vehiculos_sucursal.get(id_vehiculo)
    if vehiculos_id is None:
        print(f"No tenemos un vehículo con la ID ingresada")
        return
    if not vehiculos_id["alquilado"]:
        print(f"El vehículo con la ID: {id_vehiculo} no ha sido alquilado")
        return
    modelo = vehiculos_id["modelo"]
    vehiculos_id["alquilado"] = False
    print(f"El vehículo {modelo} con la ID: {id_vehiculo} ha sido devuelto exitosamente")
    return

def mostrar_flota(flota):
    for sucursal in flota:
        for id_vehiculo in flota[sucursal]:
            modelo = flota[sucursal][id_vehiculo]["modelo"]
            precio = flota[sucursal][id_vehiculo]["precio_dia"]
            estado = flota[sucursal][id_vehiculo]["alquilado"]
            if estado:
                print(f"Vehículo: {modelo}, Precio: {precio}, Sucursal: {sucursal}, Alquilado")
            else:
                print(f"Vehículo: {modelo}, Precio: {precio}, Sucursal: {sucursal}, Disponible")
    return

#Estructura de datos

flota = {
    "Centro": {
        "V-101": {"modelo": "Toyota Corolla", "precio_dia": 40.0, "alquilado": False},
        "V-102": {"modelo": "Ford Fiesta", "precio_dia": 25.0, "alquilado": True}
    },
    "Norte": {
        "V-201": {"modelo": "Honda Civic", "precio_dia": 50.0, "alquilado": False}
    } 
}

# Diccionario global de códigos de descuento promocionales

DESCUENTOS = {
    "VERANO10": 0.10,  # 10% de descuento
    "PROMO20": 0.20    # 20% de descuento
}

#Flujo del programa

menu(flota)