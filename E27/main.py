"""Main.py"""

if __name__ == "__main__":
    import pickle
    from pathlib import Path
    from estrategias import ComisionFija, ComisionPorcentual
    from excepciones import ActivoExistenteError, ActivoNoEncontrado, FondosInsuficientesError, OperacionInvalidaError
    from modelos import Accion, Criptomoneda, Bono
    from portafolio import Portafolio
    
    def guardar_datos(ruta, datos: Portafolio) -> None:
        """Función de guardado de datos"""
        with open(ruta, "wb") as archivo:
            pickle.dump(datos, archivo)
        return

    def cargar_datos(ruta) -> Portafolio:
        """Función de carga de datos"""
        try:
            with open(ruta, "rb") as archivo: 
                return pickle.load(archivo)
        except (FileNotFoundError, pickle.PickleError):
            return Portafolio([], 0)    

    def menu() -> None:
        "Función que se encarga del menú principal del programa"
        while True:
            print("\n---Menú---")
            print("1. Agregar activo al portafolio")
            print("2. Comprar más activos")
            print("3. Calcular valor total del portafolio")
            print("4. Guardar cambios")
            print("5. Añadir saldo al portafolio")
            print("6. Ver activos en el portafolio")
            print("7. Salir")
            try:
                opcion = float(input("Introduce una de las opciones mostradas en el menú: "))
            except ValueError:
                print("Introduce uno de los números que aparecen para elegir.")
                continue
            match opcion:
                case 1:
                    """Agregar activo"""
                    menu_1()
                    continue
                case 2:
                    """Comprar activo"""
                    menu_2()
                    continue
                case 3:
                    """Calcular valor total del portafolio"""
                    print(f"Valor total del portafolio: {portafolio_base.calcular_valor_total_portafolio()}$")
                    continue
                case 4: 
                    guardar_datos(ruta, portafolio_base)
                    print("Datos guardados exitosamente")
                    continue
                case 5:
                    try:
                        saldo_nuevo = float(input("Introduce el saldo que vas a añadir al portafolio: "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    try:
                        portafolio_base.saldo_efectivo = saldo_nuevo
                    except OperacionInvalidaError:
                        print("Introduce un número mayor a 0.")
                        continue
                    print("Saldo añadido exitosamente")
                    continue
                case 6:
                    print("---Porfafolio---")
                    for activo in portafolio_base:
                        print(activo)
                    continue
                case 7:
                    """Salir del programa"""
                    print("Saliendo...")
                    break
                case _:
                    """Cualquier otro caso"""
                    print("Introduce uno de los números que aparecen para elegir.")
                    continue

    def menu_1():
        """Menú que se encarga de gestionar la adición por primera vez de activos al portafolio"""
        while True:
            print("\n1. Agregar acciones al portafolio")
            print("2. Agregar criptomonedas al portafolio")
            print("3. Agregar bonos al portafolio")
            print("4. Volver al menú anterior")
            try:
                opcion_1 = float(input("Introduce una de las opciones mostradas en el menú: "))
            except ValueError:
                print("Introduce uno de los números que aparecen para elegir.")
                continue
            match opcion_1:
                case 1:
                    """Agregar acciones"""
                    simbolo = input("¿Cuál es el ID de las acciones? ")
                    nombre = input("¿Cuál es el nombre de la empresa? ")
                    try:
                        precio_actual = float(input("¿Cuál es el precio unitario de las acciones de esta empresa? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    try:
                        cantidad = float(input("¿Cuántas desea comprar? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    respuestas_comision_fija = ["fija", "comisión fija", "comision fija"]
                    respuestas_comision_porcentual = ["porcentual", "comisión porcentual", "comision porcentual"]
                    while True:
                        comision_opcion = input("¿La comisión es fija o porcentual? ")
                        if comision_opcion.lower() in respuestas_comision_fija:
                            estrategia_comision = ComisionFija()
                            break
                        if comision_opcion.lower() in respuestas_comision_porcentual:
                            estrategia_comision = ComisionPorcentual()
                            break
                        print("Intente de nuevo. Si es comisión fija, responda fija, si es comisión porcentual responda porcentual.")
                        continue
                    sector = input("¿A cuál sector pertenece la empresa de estas acciones? ")
                    try:
                        portafolio_base.agregar_activo(Accion(simbolo, nombre, precio_actual, cantidad, estrategia_comision, sector))
                    except ActivoExistenteError as e:
                        print(e)
                        print(f"ID del activo: {e.simbolo}")
                        continue
                    except FondosInsuficientesError as e:
                        print(e)
                        print(f"Saldo actual: {e.saldo_disponible} | Monto requerido: {e.monto_requerido}")
                        continue
                    except OperacionInvalidaError as e:
                        print(e)
                        continue
                    print(f"Han sido agregadas {cantidad} acciones de la empresa {nombre} con ID: {simbolo} al portafolio")
                    continue
                case 2:
                    """Agregar criptomonedas"""
                    simbolo = input("¿Cuál es el ID de la esta criptomoneda?")
                    nombre = input("¿Cuál es el nombre de la criptomoneda?")
                    try:
                        precio_actual = float(input("¿Cuál es el precio unitario de la criptomoneda? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    try:
                        cantidad = float(input("¿Cuántas desea comprar? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    respuestas_comision_fija = ["fija", "comisión fija", "comision fija"]
                    respuestas_comision_porcentual = ["porcentual", "comisión porcentual", "comision porcentual"]
                    while True:
                        comision_opcion = input("¿La comisión es fija o porcentual? ")
                        if comision_opcion.lower() in respuestas_comision_fija:
                            estrategia_comision = ComisionFija()
                            break
                        if comision_opcion.lower() in respuestas_comision_porcentual:
                            estrategia_comision = ComisionPorcentual()
                            break
                        print("Intente de nuevo. Si es comisión fija, responda fija, si es comisión porcentual responda porcentual.")
                        continue
                    try:
                        volatilidad = float(input("¿Cuál es la volatilidad de esta criptomoneda? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    try:
                        portafolio_base.agregar_activo(Criptomoneda(simbolo, nombre, precio_actual, cantidad, estrategia_comision, volatilidad))
                    except ActivoExistenteError as e:
                        print(e)
                        print(f"ID del activo: {e.simbolo}")
                        continue
                    except FondosInsuficientesError as e:
                        print(e)
                        print(f"Saldo actual: {e.saldo_disponible} | Monto requerido: {e.monto_requerido}")
                        continue
                    except OperacionInvalidaError as e:
                        print(e)
                        continue
                    print(f"Han sido agregadas {cantidad} criptomonedas de nombre {nombre} con ID: {simbolo} al portafolio")
                    continue
                case 3:
                    """Agregar Bono"""
                    nombre = input("¿Cuál es el nombre de la empresa? ")
                    try:
                        precio_actual = float(input("¿Cuál es el precio unitario de los bonos de esta empresa? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    try:
                        cantidad = float(input("¿Cuántas desea comprar? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    respuestas_comision_fija = ["fija", "comisión fija", "comision fija"]
                    respuestas_comision_porcentual = ["porcentual", "comisión porcentual", "comision porcentual"]
                    while True:
                        comision_opcion = input("¿La comisión es fija o porcentual? ")
                        if comision_opcion.lower() in respuestas_comision_fija:
                            estrategia_comision = ComisionFija()
                            break
                        if comision_opcion.lower() in respuestas_comision_porcentual:
                            estrategia_comision = ComisionPorcentual()
                            break
                        print("Intente de nuevo. Si es comisión fija, responda fija, si es comisión porcentual responda porcentual.")
                        continue
                    try:
                        tasa_interes = float(input("¿Cuál es la tasa de interés de los bonos? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    try:
                        portafolio_base.agregar_activo(Bono(simbolo, nombre, precio_actual, cantidad, estrategia_comision, tasa_interes))
                    except ActivoExistenteError as e:
                        print(e)
                        print(f"ID del activo: {e.simbolo}")
                        continue
                    except FondosInsuficientesError as e:
                        print(e)
                        print(f"Saldo actual: {e.saldo_disponible} | Monto requerido: {e.monto_requerido}")
                        continue
                    except OperacionInvalidaError as e:
                        print(e)
                        continue
                    print(f"Han sido agregados {cantidad} bonos de la empresa {nombre} con ID: {simbolo} al portafolio")
                    continue
                case 4:
                    """Salir del submenú"""
                    print("Volviendo al menú anterior...")
                    break
                case _:
                    """Cualquier otro caso"""
                    print("Introduce uno de los números que aparecen para elegir.")
                    continue

    def menu_2():
        """Menú que se encarga de gestionar las compras de activos al portafolio"""
        while True:
            print("\n1. Comprar acciones")
            print("2. Comprar criptomonedas")
            print("3. Comprar bonos")
            print("4. Volver al menú anterior")
            try:
                opcion_2 = float(input("Introduce una de las opciones mostradas en el menú: "))
                if not isinstance(opcion_2, float):
                    raise TypeError
            except TypeError:
                print("Introduce uno de los números que aparecen para elegir.")
                continue
            match opcion_2:
                case 1:
                    """Comprar acciones"""
                    simbolo = input("¿Cuál es el ID de las acciones? ")
                    try:
                        cantidad = float(input("¿Cuántas desea comprar? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    try:
                        portafolio_base.comprar_activo(simbolo, cantidad)
                    except ActivoNoEncontrado as e:
                        print(e)
                        print(f"ID del activo: {e.simbolo}")
                        continue
                    except FondosInsuficientesError as e:
                        print(e)
                        print(f"Saldo actual: {e.saldo_disponible} | Monto requerido: {e.monto_requerido}")
                        continue
                    except OperacionInvalidaError as e:
                        print(e)
                        continue
                    print(f"Han sido agregadas {cantidad} acciones con ID: {simbolo} al portafolio")
                    continue
                case 2:
                    """Comprar criptomonedas"""
                    simbolo = input("¿Cuál es el ID de las criptomonedas? ")
                    try:
                        cantidad = float(input("¿Cuántas desea comprar? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    try:
                        portafolio_base.comprar_activo(simbolo, cantidad)
                    except ActivoNoEncontrado as e:
                        print(e)
                        print(f"ID del activo: {e.simbolo}")
                        continue
                    except FondosInsuficientesError as e:
                        print(e)
                        print(f"Saldo actual: {e.saldo_disponible} | Monto requerido: {e.monto_requerido}")
                        continue
                    except OperacionInvalidaError as e:
                        print(e)
                        continue
                    print(f"Han sido agregadas {cantidad} con ID: {simbolo} al portafolio")
                    continue
                case 3:
                    """Comprar bonos"""
                    simbolo = input("¿Cuál es el ID de los bonos? ")
                    try:
                        cantidad = float(input("¿Cuántas desea comprar? "))
                    except ValueError:
                        print("Introduce un número mayor a 0.")
                        continue
                    try:
                        portafolio_base.agregar_activo(simbolo, cantidad)
                    except ActivoExistenteError as e:
                        print(e)
                        print(f"ID del activo: {e.simbolo}")
                        continue
                    except FondosInsuficientesError as e:
                        print(e)
                        print(f"Saldo actual: {e.saldo_disponible} | Monto requerido: {e.monto_requerido}")
                        continue
                    except OperacionInvalidaError as e:
                        print(e)
                        continue
                    print(f"Han sido agregados {cantidad} con ID: {simbolo} al portafolio")
                    continue
                case 4:
                    """Salir del submenú"""
                    print("Volviendo al menú anterior...")
                    break
                case _:
                    """Cualquier otro caso"""
                    print("Introduce uno de los números que aparecen para elegir.")
                    continue

"""Flujo del programa"""

"""Cada vez que inicio el programa obtengo la ruta del archivo con Path, y busco la carpeta `Datos` y el archivo `datos_portafolio.pkl`
que es ahí donde se va a cargar y guardar la instancia Portafolio"""
ruta_archivo = Path(__file__).resolve()
ruta_raiz = ruta_archivo.parent
ruta = ruta_raiz / "Datos" / "datos_portafolio.pkl"
portafolio_base = cargar_datos(ruta)
"""Luego, se abre el menú donde el usuario interactúa con su portafolio."""
menu()