import pickle
from pathlib import Path

def menu():
    while True:
        print("\n---Gestión de flota---")
        print("1. Registrar vehículo")
        print("2. Buscar vehículo")
        print("3. Actualizar kilometraje de un vehículo")
        print("4. Calcular costo total del mantenimiento")
        print("5. Guardar cambios")
        print("6. Generar reporte")
        print("7. Salir")

        try:
            opcion = int(input("Introduce la opción que vas a elegir: "))
        except ValueError:
            print("Tienes que introducir uno de los números de las opciones que aparecen en el menú")
            continue

        match opcion:
            case 1:
                while True:
                    print("1. Registrar un Camion")
                    print("2. Registrar una Furgoneta")
                    print("3. Registrar una Motocicleta")
                    try:
                        opcion_2 = int(input("Introduce la opción que vas a elegir: "))
                    except ValueError:
                        print("Tienes que introducir uno de los números de las opciones que aparecen en el menú")
                        continue
                    match opcion_2:
                        case 1:
                            placa = input("Introduce la placa del camión: ")
                            marca = input("Introduce la marca del camión: ")
                            try:
                                kilometraje = float(input("Introduce el kilometraje del camión: "))
                            except ValueError:
                                print("Introduce un número como kilometraje")
                                continue
                            if kilometraje <= 0.0:
                                print("El kilometraje tiene que ser mayor o igual a 0")
                                continue
                            try:
                                costo_base_mantenimiento = float(input("Introduce el costo base del mantenimiento: "))
                            except ValueError:
                                print("Introduce un número como costo base del mantenimiento")
                                continue
                            if costo_base_mantenimiento < 0.0:
                                print("Introduce un costo base del mantenimiento mayor a 0")
                                continue
                            try:
                                capacidad_toneladas = float(input("Introduce la capacidad de toneladas del camión: "))
                            except ValueError:
                                print("Introduce un número como capacidad de toneladas")
                                continue
                            if capacidad_toneladas < 0.0:
                                print("Introduce una capacidad de toneladas mayor a 0")
                                return
                            vehiculo = Camion(placa, marca, kilometraje, costo_base_mantenimiento, capacidad_toneladas)
                            empresa.registrar_vehiculo(vehiculo)
                            break
                        case 2:
                            placa = input("Introduce la placa de la furgoneta: ")
                            marca = input("Introduce la marca de la furgoneta: ")
                            try:
                                kilometraje = float(input("Introduce el kilometraje de la furgoneta: "))
                            except ValueError:
                                print("Introduce un número como kilometraje")
                                continue 
                            if kilometraje <= 0.0:
                                print("El kilometraje tiene que ser mayor o igual a 0")
                                continue
                            try:
                                costo_base_mantenimiento = float(input("Introduce el costo base del mantenimiento: "))
                            except ValueError:
                                print("Introduce un número como costo base del mantenimiento")
                                continue
                            if costo_base_mantenimiento < 0.0:
                                print("Introduce un costo base del mantenimiento mayor a 0")
                                continue
                            opcion_furgoneta = input("¿Es refrigerada? ")
                            while True:
                                match opcion_furgoneta:
                                    case "Si":
                                        es_refrigerada = True
                                        break
                                    case "SI":
                                        es_refrigerada = True
                                        break
                                    case"sI":
                                        es_refrigerada = True
                                        break
                                    case "si":
                                        es_refrigerada = True
                                        break
                                    case "No":
                                        es_refrigerada = False
                                        break
                                    case "NO":
                                        es_refrigerada = False
                                        break
                                    case "nO":
                                        es_refrigerada = False
                                        break
                                    case "no":
                                        es_refrigerada = False
                                        break
                                    case _:
                                        print("Introduce si o no")
                                        continue
                            vehiculo = Furgoneta(placa, marca, kilometraje, costo_base_mantenimiento, es_refrigerada)
                            empresa.registrar_vehiculo(vehiculo)
                            break                           
                        case 3:
                            placa = input("Introduce la placa de la motocicleta: ")
                            marca = input("Introduce la marca de la motocicleta: ")
                            try:
                                kilometraje = float(input("Introduce el kilometraje de la motocicleta: "))
                            except ValueError:
                                print("Introduce un número como kilometraje")
                                continue 
                            if kilometraje <= 0.0:
                                print("El kilometraje tiene que ser mayor o igual a 0")
                                continue
                            try:
                                costo_base_mantenimiento = float(input("Introduce el costo base del mantenimiento: "))
                            except ValueError:
                                print("Introduce un número como costo base del mantenimiento")
                                continue
                            if costo_base_mantenimiento < 0.0:
                                print("Introduce un costo base del mantenimiento mayor a 0")
                                continue
                            try:
                                cilindrada = int(input("Introduce la cilindrada de la motocicleta: "))
                            except ValueError:
                                print("Introduce un número entero como cilindrada")
                                continue
                            if cilindrada <= 0:
                                print("Introduce una cilindrada mayor a 0")
                                continue
                            vehiculo = Motocicleta(placa, marca, kilometraje, costo_base_mantenimiento, cilindrada)
                            empresa.registrar_vehiculo(vehiculo)
                            break                           
                        case _:
                            print("Elige una de las opciones que aparece en el menú")
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                print("Saliendo...")
                break
            case _:
                print("Elige una de las opciones que aparece en el menú")
    return

def cargar_datos(ruta):
    try:
        with open(ruta, "rb") as archivo:
            return pickle.load(archivo)
    except (FileNotFoundError, pickle.PickleError):
        return EmpresaLogistica()

def guardar_datos(ruta, datos):
    with open(ruta, "wb") as archivo:
        pickle.dump(datos, archivo)
    print("Datos guardados exitosamente")
    return

#Flujo del programa

ruta_archivo = Path(__file__).resolve()
ruta_raiz = ruta_archivo.parent
ruta = ruta_raiz / "Datos" / "datos_empresa.pkl"
empresa = cargar_datos(ruta)
menu()
