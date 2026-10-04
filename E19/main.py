import sys
import pickle
from clases import Estudiante, Institucion, Gestor_Academico

def menu():
    while True:
        print("\n---Gestión de Instituciones---")
        print("1. Agregar institución")
        print("2. Eliminar institución")
        print("3. Gestionar estudiantes")
        print("4. Mostrar instituciones")
        print("5. Guardar cambios")
        print("6. Buscar institución")
        print("7. Salir")

        try:
            opcion = int(input("Introduce la opción que vas a elegir: "))
        except ValueError:
            print("Tienes que introducir uno de los números de las opciones que aparecen en el menú")
            continue

        match opcion:
            case 1:
                nombre = input("Introduce el nombre de la institución: ")
                materias_validas = [] #"MAT101", "PROG101", "FIS101"
                while True:
                    materia = input("Introduce la materia a añadir a la institución (Introduce 0 para no añadir más materias): ").upper()
                    if materia in materias_validas:
                        print("Ya introduciste esa materia a la institución")
                        continue
                    if materia == "0":
                        break
                    materias_validas.append(materia)
                gestor.agregar_institucion(nombre, materias_validas)
            case 2:
                nombre = input("Introduce el nombre de la institución: ")
                gestor.eliminar_institucion(nombre)
            case 3:
                menu_1()
            case 4:
                gestor.mostrar_instituciones()
            case 5:
                guardar_datos(ruta, gestor)
            case 6:
                nombre = input("Introduce el nombre de la institución: ")
                gestor.buscar_institucion(nombre)
            case 7:
                print("Saliendo...")
                break
            case _:
                print("Elige una de las opciones que aparece en el menú")
    return

def menu_1():
    while True:
        print("\n---Gestión de Estudiantes---")
        print("1. Agregar estudiante")
        print("2. Inscribir materia")
        print("3. Retirar materia")
        print("4. Eliminar estudiante")
        print("5. Buscar estudiante")
        print("6. Mostrar estudiantes")
        print("7. Guardar cambios")
        print("8. Volver al menú anterior")
        print("9. Salir")

        try:
            opcion = int(input("Introduce la opción que vas a elegir: "))
        except ValueError:
            print("Tienes que introducir uno de los números de las opciones que aparecen en el menú")
            continue

        match opcion:
            case 1:
                id_estudiante = input("Introduce el ID que se le va a asignar al estudiante: ")
                nombre = input("Introduce el nombre del estudiante: ")
                institucion = input("Introduce el nombre de la institución: ")
                try:
                    institucion_buscada = gestor.buscar_institucion_obj(institucion)
                    institucion_buscada.agregar_estudiante(nombre, id_estudiante)
                except AttributeError:
                    print("Ingresa una institución válida")
                    continue
            case 2:
                id_estudiante = input("Introduce el ID del estudiante: ")
                nombre = input("Introduce el nombre del estudiante: ")
                institucion = input("Introduce el nombre de la institución: ")
                codigos_materia = input("Introduce el código de la materia a inscribir: ")
                try:
                    institucion_buscada = gestor.buscar_institucion_obj(institucion)
                    _ = institucion_buscada.nombre
                except AttributeError:
                    print("Ingresa una institución válida")
                    continue
                try:
                    estudiante_buscado = institucion_buscada.buscar_estudiante_obj(id_estudiante)
                    estudiante_buscado.inscribir_materia(institucion_buscada, codigos_materia)
                except AttributeError:
                    print("Ingresa un estudiante válido")
                    continue
            case 3:
                id_estudiante = input("Introduce el ID del estudiante: ")
                nombre = input("Introduce el nombre del estudiante: ")
                codigos_materia = input("Introduce el código de la materia a inscribir: ")
                institucion = input("Introduce el nombre de la institución: ")
                try:
                    institucion_buscada = gestor.buscar_institucion_obj(institucion)
                    _ = institucion_buscada.nombre
                except AttributeError:
                    print("Ingresa una institución válida")
                    continue
                try:
                    estudiante_buscado = institucion_buscada.buscar_estudiante_obj(id_estudiante) 
                    estudiante_buscado.retirar_materia(institucion_buscada, codigos_materia)
                except AttributeError:
                    print("Ingresa un estudiante válido")
                    continue
            case 4:
                id_estudiante = input("Introduce el ID del estudiante que se desea eliminar: ")
                nombre = input("Introduce el nombre del estudiante que se desea eliminar: ")
                institucion = input("Introduce el nombre de la institución: ")
                try:
                    institucion_buscada = gestor.buscar_institucion_obj(institucion)
                    institucion_buscada.eliminar_estudiante(nombre, id_estudiante)
                except AttributeError:
                    print("Ingresa una institución válida")
                    continue
            case 5:
                id_estudiante = input("Introduce el ID del estudiante: ")
                nombre = input("Introduce el nombre del estudiante: ")
                institucion = input("Introduce el nombre de la institución: ")
                try:
                    institucion_buscada = gestor.buscar_institucion_obj(institucion)
                    institucion_buscada.buscar_estudiante(nombre, id_estudiante)
                except AttributeError:
                    print("Ingresa una institución válida")
                    continue
            case 6:
                institucion = input("Introduce el nombre de la institución: ")
                try:
                    institucion_buscada = gestor.buscar_institucion_obj(institucion)
                    institucion_buscada.mostrar_estudiantes()  
                except AttributeError:
                    print("Ingresa una institución válida")
                    continue
            case 7:
                guardar_datos(ruta, gestor)
            case 8:
                break
            case 9:
                print("Saliendo...")
                sys.exit()
            case _:
                print("Elige una de las opciones que aparece en el menú")
    return

def cargar_datos(ruta):
    try:
        #Estructura de datos en disco

        with open(ruta, "rb") as archivo:
            return pickle.load(archivo)
    except(FileNotFoundError, pickle.PickleError, EOFError):

        #Estructura de datos por defecto

         return Gestor_Academico()

def guardar_datos(ruta, datos):
    with open(ruta, "wb") as archivo:
        pickle.dump(datos, archivo)
    print("Datos guardados exitosamente")
    return

#Flujo del programa

if __name__ == "__main__":
    ruta = r"C:\Users\USUARIO\Downloads\Programacion\Python\E19\archivos\datos_gestor"
    gestor = cargar_datos(ruta)
    menu()