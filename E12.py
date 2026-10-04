
#Funciones
  
def prestar_libro(biblioteca):
    categoria = input("¿De que categoria es el libro que buscas? ")
    titulo = input("¿Cual es el nombre del libro que buscas? ")    
    if categoria in biblioteca:
        if titulo in biblioteca[categoria]:
            if biblioteca[categoria][titulo]["disponibles"] > 0:
                biblioteca[categoria][titulo]["disponibles"] = biblioteca[categoria][titulo]["disponibles"] - 1
                biblioteca[categoria][titulo]["prestados"] = biblioteca[categoria][titulo]["prestados"] + 1
                print(f"Se ha prestado una copia del libro: {titulo} de la categoria {categoria}, quedan disponibles {biblioteca[categoria][titulo]["disponibles"]} y hemos prestado {biblioteca[categoria][titulo]["prestados"]}")
            elif biblioteca[categoria][titulo]["disponibles"] == 0:
                print(f"Hemos prestado todas las copias del libro: {titulo}")
        else: 
            print(f"No tenemos copias de ese libro en esta categoria")
    else:
        print("No existe esa categoria en esta biblioteca")
    return
    
def agregar_o_quitar_libro(biblioteca):
    categoria = input("¿A cual categoria deseas agregar o quitar el libro? ")
    titulo = input("¿Cual es el nombre del libro que deseas agregar o quitar? ") 
    copias = int(input(f"¿Cuantas copias de {titulo} quieres agregar o quitar a la categoria {categoria}? (Si deseas quitar escribe un número negativo) "))

    biblioteca[categoria] = biblioteca.setdefault(categoria, {})
    if titulo in biblioteca[categoria]:
        if copias >= - (biblioteca[categoria][titulo]["disponibles"]):
            biblioteca[categoria][titulo] = {"disponibles": biblioteca[categoria][titulo]["disponibles"] + copias, "prestados" :  biblioteca[categoria][titulo]["prestados"]}
        else:
            print("No se pueden quitar más copiar de los que tenemos")
    elif titulo not in biblioteca[categoria]:
        if copias > 0: 
            biblioteca[categoria][titulo] = {"disponibles": copias, "prestados": 0}
        else:
            print("Debes de añadir aunque sea una copia a la categoria")
    return

def mostrar_libros_por_categoria(biblioteca):
    for categoria, libros in biblioteca.items():
        for titulo in libros:
            cantidad = biblioteca[categoria][titulo]["disponibles"]
            prestamos = biblioteca[categoria][titulo]["prestados"]

            print(f"Titulo: {titulo}, Cantidad: {cantidad}, Prestamos: {prestamos}, Categoria: {categoria}" )
    return

def devolver_libro(biblioteca):
    categoria = input("¿De cual categoria es el libro? ")
    titulo = input("¿Cual es el libro que deseas devolver? ")
    
    if categoria in biblioteca:
        if titulo in biblioteca[categoria]:
            if biblioteca[categoria][titulo]["prestados"] > 0:
                biblioteca[categoria][titulo]["prestados"] = biblioteca[categoria][titulo]["prestados"] - 1
                biblioteca[categoria][titulo]["disponibles"] = biblioteca[categoria][titulo]["disponibles"] + 1
                print(f"Se ha devuelto exitosamente el libro: {titulo}, quedan disponibles {biblioteca[categoria][titulo]["disponibles"]} y hemos prestado {biblioteca[categoria][titulo]["prestados"]}")
            else:
                print(f"No hemos prestado ninguna copia del libro: {titulo}")
        elif titulo not in biblioteca[categoria]:
            print("No ofrecemos copias de ese libro en esta categoria")
    else:
        print("No tenemos esa categoria en esta biblioteca")
    return

def eliminar_libro(biblioteca):
    categoria = input("¿De cual categoria es el libro que quieres eliminar? ")
    titulo = input("¿Cual es el libro que deseas eliminar? ")

    if categoria in biblioteca:
        if titulo in biblioteca[categoria]:
            if biblioteca[categoria][titulo]["prestados"] == 0:
                del(biblioteca[categoria][titulo])
                print(f"Se ha eliminado satisfactoriamente {titulo} de la categoria {categoria}")
            else:
                print(f"Hemos prestado {biblioteca[categoria][titulo]["prestados"]} copias de {titulo}, por ende no lo podemos eliminar")
        else:
            print(f"No tenemos el libro {titulo} en la biblioteca")
    else:
        print("No tenemos esa categoria en esta biblioteca")
    return

#Estructuras de datos

biblioteca = {"Programacion" : {"Python Intenso" : {"disponibles" : 5, "prestados" : 0}, "C++ Basico" : {"disponibles" : 2, "prestados" : 1 }}, "Matematicas" : {"Calculo I" : {"disponibles" : 4, "prestados" : 2}}}

#Menú del programa

abierto = True
opcion = 0
while abierto:
    print("Gestor de Prestamos de Biblioteca")
    print("1. Prestar un libro")
    print("2. Agregar, actualizar o quitar libro")
    print("3. Mostrar libros disponibles de una categoria")
    print("4. Devolver un libro")
    print("5. Eliminar un libro de una categoria")
    print("6. Salir")
    opcion = int(input("¿Cual opcion vas a elegir? "))
    print(" ")
    if opcion == 1:
        prestar_libro(biblioteca)
        print(" ")
    elif opcion == 2:
        agregar_o_quitar_libro(biblioteca)
        print(" ")
    elif opcion == 3:
        mostrar_libros_por_categoria(biblioteca)
        print(" ")
    elif opcion == 4:
        devolver_libro(biblioteca)
        print(" ")
    elif opcion == 5:
        eliminar_libro(biblioteca)
        print(" ")
    elif opcion ==  6:
        abierto = False
        print("Saliendo...")
    else:
        print("Elige una de las opciones mostradas")
        print(" ")
        opcion = 0