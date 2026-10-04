
#Archivos y funciones

from gestion_academica import (
    registrar_estudiante,
    inscribir_materia,
    mostrar_resumen,
    eliminar_estudiante,
    guardar_datos,
    CLAVES_VALIDAS,
    estudiantes,
    inscripciones
)

def menu():
    while True:
        print("\n---Sistema Académico Modular---")
        print("1. Registrar estudiante")
        print("2. Inscribir materia")
        print("3. Eliminar estudiante")
        print("4. Mostrar resumen")
        print("5. Guardar cambios")
        print("6. Salir")

        try:
            opcion = int(input("Introduce la opción que vas a elegir: "))
        except ValueError:
            print("Tienes que introducir uno de los números de las opciones que aparecen en el menú")
            continue

        match opcion:
            case 1:
                id_estudiante = input("Introduce el ID que se le va a asignar al estudiante: ")
                nombre = input("Introduce el nombre del estudiante: ")
                registrar_estudiante(id_estudiante, nombre)
            case 2:
                id_estudiante = input("Introduce el ID del estudiante: ")
                codigos_materia = input("Introduce el código de la materia a inscribir: ")
                inscribir_materia(id_estudiante, codigos_materia)
            case 3:
                id_estudiante = input("Introduce el ID del estudiante que se desea eliminar: ")
                nombre = input("Introduce el nombre del estudiante que se desea eliminar: ")
                eliminar_estudiante(id_estudiante, nombre)
            case 4:
                mostrar_resumen()
            case 5:
                guardar_datos(CLAVES_VALIDAS, estudiantes, "estudiantes") 
                guardar_datos(CLAVES_VALIDAS, inscripciones, "inscripciones")
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Elige una de las opciones que aparece en el menú")
    return

#Flujo del programa
if __name__ == "__main__":
    menu()