#Funciones

def agregar_tarea(proyectos, area, id_tarea, descripcion):
    proyectos.setdefault(area, {})
    if id_tarea in proyectos[area]:
        print(f"La tarea {id_tarea} ya existe en el área {area}")
        return
    proyectos[area][id_tarea] = {"descripcion" : descripcion, "completada": False}
    print(f"Se ha creado exitosamente la tarea con ID: {id_tarea} y descripción: {descripcion}")
    return
    
def marcar_completada(proyectos, area, id_tarea):
    if area not in proyectos:
        print("No tenemos esa área")
        return
    if id_tarea not in proyectos[area]:
        print(f"No hay ninguna tarea con el ID {id_tarea} en {area}")
        return
    if proyectos[area][id_tarea]["completada"]:
        print(f"La tarea con ID: {id_tarea} ya ha sido completada anteriormente")
        return
    proyectos[area][id_tarea]["completada"] = True
    print(f"Se ha completado exitosamente la tarea con ID: {id_tarea} en {area}")
    return

def mostrar_tareas(proyectos):
    for area in proyectos:
        for id_tarea in proyectos[area]:
            descripcion = proyectos[area][id_tarea]["descripcion"]
            estado = proyectos[area][id_tarea]["completada"]
            if estado:
                print(f"ID: {id_tarea}, Área: {area}, Descripción: {descripcion}, Estado: Completada")
                
            else:
                print(f"ID: {id_tarea}, Área: {area}, Descripción: {descripcion}, Estado: No completada")
    return

#Estructuras de datos

proyectos = {
    "Desarrollo": {
        "T1": {"descripcion": "Diseñar base de datos", "completada": False},
        "T2": {"descripcion": "Crear API REST", "completada": True}
    },
    "Diseno": {
        "T3": {"descripcion": "Crear prototipo Figma", "completada": False}
    }
}

#Menu general del programa

abierto = True
opcion = 0
while abierto:
    print("Gestor de Proyectos y Tareas por área")
    print("1. Agregar tarea o marcar completada una tarea")
    print("2. Mostrar tareas")
    print("3. Salir")
    opcion = int(input("¿Cuál opción vas a elegir? "))
    print(" ")
    if opcion == 1:
        
        #Menu de modificación de tareas

        abierto_2 = True
        opcion_2 = 0
        area = input("Introduce el área del proyecto al que pertenece la tarea: ")
        id_tarea = input("Introduce el ID de la tarea: ")
        descripcion = input("Introduce su descripción (Si deseas agregar la tarea): ")
        while abierto_2:
            print("1. Agregar la tarea")
            print("2. Marcar completada la tarea")
            print("3. Volver hacia atrás")
            print("4. Salir")
            opcion_2 = int(input("¿Cuál opción vas a elegir? "))
            if opcion_2 == 1:
                agregar_tarea(proyectos, area, id_tarea, descripcion)
                print(" ")
            elif opcion_2 == 2:
                marcar_completada(proyectos, area, id_tarea)
                print(" ")
            elif opcion_2 == 3:
                print(" ")
                break
            elif opcion_2 == 4:
                abierto = False
                abierto_2 = False
                print("Saliendo...")
            else:
                print("Elige una de las opciones mostradas")
                print(" ")
                
    elif opcion == 2:
        mostrar_tareas(proyectos)
        print(" ")
    elif opcion ==  3:
        abierto = False
        print("Saliendo...")
    else:
        print("Elige una de las opciones mostradas")
        print(" ")
        opcion = 0