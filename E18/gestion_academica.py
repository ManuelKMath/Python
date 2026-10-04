#Librerías

import sys
import json

#Funciones

def registrar_estudiante(id_estudiante, nombre):
    ficha = (id_estudiante, nombre)

    for info_estudiantes in estudiantes:
        if id_estudiante == info_estudiantes[0]:
            estudiante_actual = info_estudiantes[1]
            print(f"La id: {id_estudiante} ya está asignada al estudiante {estudiante_actual}")
            return
    estudiantes.append(ficha)
    inscripciones[id_estudiante] = []
    print(f"El estudiante {nombre} ha sido registrado con la ID: {id_estudiante}")
    return

def inscribir_materia(id_estudiante, codigos_materia):
    if codigos_materia.upper() not in MATERIAS_VALIDAS:
        print(f"El código {codigos_materia.upper()} no le corresponde a ninguna materia de esta institución")
        return
    if id_estudiante not in inscripciones:
        print("La ID introducida no es de ningún estudiante de esta institución")
        return
    if codigos_materia.upper() in inscripciones[id_estudiante]:
        print(f"El estudiante con ID: {id_estudiante} ya tiene inscrita la materia con código: {codigos_materia.upper()}")
        return
    inscripciones[id_estudiante].append(codigos_materia.upper())
    print(f"Se ha inscrito la materia con el código: {codigos_materia.upper()} al estudiante con la ID: {id_estudiante}")
    return

def mostrar_resumen():
    if estudiantes == []:
        print("No hay estudiantes inscritos")
        return
    for id_estudiante in inscripciones:
        if inscripciones[id_estudiante] == []:
            print(f"ID:{id_estudiante}, Materia: ")
            return
        for codigos_materia in inscripciones[id_estudiante]:
            print(f"ID:{id_estudiante}, Materia: {codigos_materia}")
    return

def eliminar_estudiante(id_estudiante, nombre):
    ficha = (id_estudiante, nombre)
    if ficha not in estudiantes:
        print(f"El estudiante {nombre} con ID: {id_estudiante} no está registrado en nuestra institución")
        return
    estudiantes.remove(ficha)
    del(inscripciones[id_estudiante])
    print(f"Se ha eliminado exitosamente el estudiante {nombre} con ID: {id_estudiante} de nuestra institución")
    return

def cargar_datos(claves_validas, clave):
    if clave not in claves_validas:
        print("ERROR DE CLAVE AL CARGAR ARCHIVOS")
        sys.exit()
    valor_por_defecto = claves_validas[clave]
    try:
        #Estructura de datos en disco
        with open("estudiantes_y_materias.json", "r") as archivo:
            return json.load(archivo)[clave]
        
    except(FileNotFoundError, json.JSONDecodeError):
        return valor_por_defecto
            
def guardar_datos(claves_validas, datos, clave):
    if clave not in claves_validas:
        print("ERROR DE CLAVE AL GUARDAR ARCHIVOS")
        sys.exit()
    claves_validas[clave] = datos
    with open("estudiantes_y_materias.json", "w") as archivo:
        json.dump(claves_validas, archivo, indent=4)
    return
    
#Claves de guardado
CLAVES_VALIDAS = {"estudiantes": [], "inscripciones": {}}

# Conjunto de materias válidas registradas en la institución (únicas)
MATERIAS_VALIDAS = ("MAT101", "PROG101", "FIS101")

# Lista de estudiantes registrados. Cada estudiante se guardará como una TUPLA inmutable: (id_estudiante, nombre)
estudiantes = cargar_datos(CLAVES_VALIDAS, "estudiantes")

# Diccionario de inscripciones: {id_estudiante: set(codigos_materia)} (LO CAMBIÉ PARA QUE EL VALOR FUERA UNA LISTA)
inscripciones = cargar_datos(CLAVES_VALIDAS, "inscripciones")