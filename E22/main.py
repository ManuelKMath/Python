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
                pass
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
