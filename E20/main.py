from personal import Persona, Administrativo, Docente

if __name__ == "__main__":
    personal = [Persona("Manuel", "1"), Administrativo("Pedro", "2", "Gerencia"), Docente("Pepe", "3", "Matematica")]
    for i in personal:
        i.obtener_rol()
    