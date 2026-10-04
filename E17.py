#Librerías

import json

#Funciones

def menu(estudiantes):
    while True:
        print("\n---Sistema de Notas Persistente---")
        print("1. Agregar o actualizar nota")
        print("2. Mostrar todos los estudiantes y sus notas")
        print("3. Eliminar estudiante de la lista")
        print("4. Guardar")
        print("5. Salir")

        try:
            opcion = int(input("Introduce la opción que vas a elegir: "))
        except ValueError:
            print("Tienes que introducir uno de los números de las opciones que aparecen en el menú")
            continue

        match opcion:
            case 1:

                try:
                    nombre  = input("Introduce el nombre del estudiante: ")
                    materia = input("Introduce la materia que cursa: ")
                    nota = float(input("Introduce la nota: "))
                except ValueError:
                    print("Datos no válidos, intentelo de nuevo")
                    continue

                agregar_nota(RUTA_ARCHIVO, estudiantes, nombre, materia, nota)
            case 2:
                mostrar_estudiantes(estudiantes)
            case 3:

                try:
                    nombre = input("Introduce el nombre del estudiante a eliminar: ")
                except ValueError:
                    print("Datos no válidos, intentelo de nuevo")
                    continue

                eliminar_estudiante(RUTA_ARCHIVO, estudiantes, nombre)
            case 4:
                guardar_datos(RUTA_ARCHIVO, estudiantes)
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Elige una de las opciones que aparece en el menú")
    return

def cargar_datos(ruta):
    try:
        #Estructura de datos en disco

        with open(ruta, "r") as archivo:
            return json.load(archivo)
    except(FileNotFoundError, json.JSONDecodeError):

        #Estructura de datos por defecto

         return {"Juan": {"Matematica": 18.0}, "Maria": {"Programacion": 20.0}}

def guardar_datos(ruta, datos):
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent = 4)
    print("Datos guardados exitosamente")
    return

def agregar_nota(ruta, estudiantes, nombre, materia, nota):
    estudiantes.setdefault(nombre, {})
    try:
        nota_anterior = estudiantes[nombre][materia]
        estudiantes[nombre][materia] = nota
        print(f"Se ha actualizado exitosamente la nota: {nota} de la materia: {materia} al estudiante {nombre}")
        guardar_datos(ruta, estudiantes)
        return
    except KeyError:
        estudiantes[nombre][materia] = nota
        print(f"Se ha agregado exitosamente la nota: {nota} y la materia: {materia} al estudiante: {nombre}")
        guardar_datos(ruta, estudiantes)
        return
    
def mostrar_estudiantes(estudiantes):
    for nombre in estudiantes:
        for materia in estudiantes[nombre]:
            nota = estudiantes[nombre][materia]
            print(f"Estudiante: {nombre} |  Materia = {materia} | Nota = {nota}")
    return

def eliminar_estudiante(ruta, estudiantes, nombre):
    if nombre not in estudiantes:
        print(f"El estudiante {nombre} no está en la lista")
        return
    del(estudiantes[nombre])
    print(f"Se ha eliminado exitosamente al estudiante {nombre} de la lista")
    guardar_datos(ruta, estudiantes)
    return

#Flujo del programas

#Estructura de datos   
RUTA_ARCHIVO = "notas.json"

estudiantes = cargar_datos(RUTA_ARCHIVO)

#Menú del programa

menu(estudiantes)