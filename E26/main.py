class Libro:
    """Clase que instancia los objetos Libro que son los objetos que se guardan en la instancia de la clase Biblioteca"""
    def __init__(self, isbn: str, titulo: str, paginas: int):
        self._isbn = isbn
        self._titulo = titulo
        self._paginas = paginas

    @property
    def isbn(self) -> str:
        return self._isbn
    
    @property
    def titulo(self) -> str:
        return self._titulo

    def __repr__(self) -> str:
        return f"isbn = {self._isbn}, titulo = {self._titulo}, paginas = {self._paginas}"

    def __eq__(self, objeto_2 : object) -> bool:
        if not isinstance(objeto_2, Libro):
            return False
        if self.isbn != objeto_2.isbn:
            return False
        return True

class BibliotecaError(Exception):
    """Clase base de errores"""
    pass

class LibroExistente(BibliotecaError):
    """Clase que lanza el error si intentas agregar un libro que ya está"""
    def __init__(self, libro: Libro):
        self.libro = libro
        super().__init__("Intentaste agregar un libro que ya estaba agregado")

class Biblioteca:
    """Clase que contiene la lista donde se guardan los libros y donde se le realiza modificaciones a esa estructura de datos"""
    def __init__(self):
        self._catalogo = []

    def agregar_libro(self, libro: Libro) -> None:
        if libro in self._catalogo:
            raise LibroExistente(libro)
        self._catalogo.append(libro)
        print(f"Se agregó el libro: {libro.titulo} a la biblioteca")
        return 

    def __len__(self) -> int:
        """Método que se encarga de devolver la longitud de la lista"""
        return len(self._catalogo)

    def __getitem__(self, posicion: int) -> Libro:
        """Método que se encarga de devolver un elemento en una posición específica de la lista"""
        if posicion > len(self) or posicion < 0:
            raise BibliotecaError(f"Error: Elige un libro que esté entre 0 y {len(self)}") 
        return self._catalogo[posicion]

#Flujo del programa
        
try:
    biblioteca1 = Biblioteca()
    libro1 = Libro("1", "Libro1", 10)
    libro2 = Libro("2", "Libro1.2", 1)
    libro11 = Libro("1", "Libro11", 15)
    biblioteca1.agregar_libro(libro1)
    biblioteca1.agregar_libro(libro2)
    biblioteca1.agregar_libro(libro11)
except LibroExistente as error:
    print(error)

for libro in biblioteca1:
    print(libro)

