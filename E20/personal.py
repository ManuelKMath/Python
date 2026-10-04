#clases

class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.nombre = cedula

    def obtener_rol(self):
        print("Persona genérica")
        return

class Administrativo(Persona):
    def __init__(self, nombre, cedula, dependencia):
        super().__init__(nombre, cedula)
        self.dependencia = dependencia
        
    def obtener_rol(self):
        print(f"Administrativo en {self.dependencia}")
        return

class Docente(Persona):
    def __init__(self, nombre, cedula, materia_dictada):
        super().__init__(nombre, cedula)
        self.materia_dictada = materia_dictada

    def obtener_rol(self):
        print(f"Docente de {self.materia_dictada}")
        return
