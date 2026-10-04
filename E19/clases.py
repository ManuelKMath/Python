
#Clases

class Estudiante():
    def __init__(self, nombre, id_estudiante):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.materias = []

    def __str__(self):
        if not self.materias:
            return f"ID: {self.id_estudiante} Estudiante: {self.nombre}, Materias: "
        materias_str = ", ".join(self.materias)
        return f"ID: {self.id_estudiante} Estudiante: {self.nombre}, Materias: {materias_str}"

    def inscribir_materia(self, institucion, codigo_materia):
        materia = codigo_materia.upper()
        if materia not in institucion.materias_validas:
            print("Ingresa un código de materia válido")
            return
        if materia in self.materias:
            print(f"El estudiante {self.nombre} ya tiene inscrita la materia con código: {materia} en la institución {institucion.nombre}")
            return
        self.materias.append(materia)
        print(f"Se ha inscrito exitosamente la materia con código: {materia} al estudiante {self.nombre} con ID: {self.id_estudiante} en la institución {institucion.nombre}")
        return
    
    def retirar_materia(self, institucion, codigo_materia):
        materia = codigo_materia.upper()
        if materia not in self.materias:
            print(f"El estudiante {self.nombre} con ID: {self.id_estudiante} no tiene esa materia inscrita")
            return
        self.materias.remove(materia)
        print(f"Se ha retirado exitosamente la materia con código: {materia} al estudiante {self.nombre} con ID: {self.id_estudiante} de la institución {institucion.nombre}")
        return
    
    def mostrar_resumen(self):
        return print(self)

class Institucion():
    def __init__(self, nombre_institucion, materias_validas):
        self.lista = []
        self.nombre = nombre_institucion
        self.materias_validas = materias_validas

    def __str__(self):
        lista_str = ", ".join(self.materias_validas)
        return f"{self.nombre} Materias = {lista_str}"

    def mostrar_estudiantes(self):
        print(f"Lista de la institución {self.nombre}")
        if not self.lista:
            print(f"No hay estudiantes registrados en la institución")
            return
        for estudiante_actual in self.lista:
            estudiante_actual.mostrar_resumen()
        return

    def agregar_estudiante(self, nombre, id_estudiante):
        try:
            _ = self.buscar_estudiante_obj(id_estudiante).nombre
            if nombre == self.buscar_estudiante_obj(id_estudiante).nombre:
                print(f"El estudiante: {nombre} ya está agregado")
                return
            print(f"La ID: {id_estudiante} ya está asignada a un estudiante distinto. Inténtelo con otra ID")
            return
        except AttributeError:
            estudiante = Estudiante(nombre, id_estudiante)
            self.lista.append(estudiante)
            print(f"Se agregó exitosamente el estudiante: {nombre} con ID: {id_estudiante} en la institución {self.nombre}")
            return

    def eliminar_estudiante(self, nombre, id_estudiante):
        if not self.lista:
            print(f"No hay estudiantes registrados en la institución")
            return
        try:
            _ = self.buscar_estudiante_obj(id_estudiante).nombre
        except AttributeError:
            print(f"No hay un estudiante registrado con la ID: {id_estudiante}")
            return
        if nombre != self.buscar_estudiante_obj(id_estudiante).nombre:
            print(f"La ID: {id_estudiante} está asignada a un estudiante distinto. Inténtelo con otra ID")
            return
        print(f"El estudiante {nombre} con ID: {id_estudiante} ha sido removido exitosamente")
        self.lista = [p for p in self.lista if p.id_estudiante != id_estudiante]
        return
    
    def buscar_estudiante(self, nombre, id_estudiante):
        if not self.lista:
            print(f"No hay estudiantes registrados en la institución {self.nombre}")
            return
        estudiante_buscado = [p for p in self.lista if p.id_estudiante == id_estudiante and p.nombre == nombre]
        if estudiante_buscado:
            return estudiante_buscado[0].mostrar_resumen()
        print(f"El estudiante {nombre} con ID: {id_estudiante} no está registrado en la institución: {self.nombre}")
        return

    def buscar_estudiante_obj(self, id_estudiante):
        estudiante_buscado = [p for p in self.lista if p.id_estudiante == id_estudiante]
        if not estudiante_buscado:
            return 
        return estudiante_buscado[0]

class Gestor_Academico():
    def __init__(self):
        self.lista_instituciones = []

    def agregar_institucion(self, nombre, materias_validas):
        if not materias_validas:
            print("No has introducido ninguna materia, Inténtelo de nuevo")
            return
        try:
            _ = self.buscar_institucion_obj(nombre).nombre
            print(f"La institucion {nombre} ya está agregada. Inténtelo de nuevo") 
            return
        except AttributeError:
            institucion = Institucion(nombre, materias_validas)
            self.lista_instituciones.append(institucion)
            print(f"La institución {nombre} ha sido agregada exitosamente")
            return
        
    def buscar_institucion(self, nombre):
        if not self.lista_instituciones:
            print("No hay instituciones registradas")
            return
        institucion_buscada = [p for p in self.lista_instituciones if p.nombre == nombre]
        if not institucion_buscada:
            print(f"La institución {nombre} no está registrada")
            return 
        return print(institucion_buscada[0])            

    def buscar_institucion_obj(self, nombre):
        institucion_buscada = [p for p in self.lista_instituciones if p.nombre == nombre]
        if not institucion_buscada:
            return 
        return institucion_buscada[0]

    def mostrar_instituciones(self):
        if not self.lista_instituciones:
            print("No hay instituciones registradas")
            return
        for institucion_actual in self.lista_instituciones:
                print(institucion_actual)
                continue
        return

    def eliminar_institucion(self, nombre):
        if not self.lista_instituciones:
            print("No hay instituciones registradas")
            return
        try:
            _ = self.buscar_institucion_obj(nombre).nombre
            print(f"La institución {nombre} fue eliminada exitosamente")
            self.lista_instituciones = [p for p in self.lista_instituciones if p.nombre != nombre]
        except AttributeError:
            print(f"La institucion {nombre} no está agregada. Inténtelo de nuevo")
            return