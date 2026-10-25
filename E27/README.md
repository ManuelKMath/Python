# Sistema de Gestión Financiera y Portafolio de Inversiones (E27)

Un sistema modular orientado a objetos escrito en Python para la administración de activos financieros (Acciones, Criptomonedas y Bonos), con cálculo polimórfico de rendimiento, estrategias dinámicas de comisión y persistencia de datos.

## 🛠️ Arquitectura y Patrones de Diseño

El proyecto está diseñado bajo los principios SOLID y la separación estricta de responsabilidades:

* **Clases Base Abstractas (`ABC`):** Definición de contratos para activos y estrategias.
* **Patrón Estrategia (Composición):** Delegación del cálculo de comisiones (`ComisionFija`, `ComisionPorcentual`) en tiempo de ejecución.
* **Jerarquía de Excepciones Personalizadas:** Control de errores de negocio sin el uso de `print()` en la capa de modelo.
* **Métodos Mágicos (`Dunder Methods`):** Métodos `__repr__`, `__eq__`, `__len__` y `__getitem__` para comportamiento nativo de colecciones.
* **Persistencia:** Carga y guardado binario mediante `pickle` y rutas portables con `pathlib.Path`.

## 📁 Estructura del Proyecto

```text
E26/
├── excepciones.py    # Jerarquía de excepciones personalizadas (FinanzasError)
├── estrategias.py    # Estrategias de comisión mediante composición (ABC)
├── modelos.py        # Dominio de activos financieros (Accion, Criptomoneda, Bono)
├── portafolio.py     # Contenedor principal de activos e iterador
├── main.py           # Interfaz CLI y manejo de excepciones
└── Datos/            # Almacenamiento del archivo de persistencia (.pkl)

🚀 Instalación y Ejecución
Clonar el repositorio:

git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)

Navegar al directorio del proyecto:

cd E27

Ejecutar el sistema principal:

python main.py

📋 Autor
Manuel Kremezis - Desarrollo e Implementación

Este fue un ejercicio bastante largo de POO con persistencia en el que pude poner en práctica un manejo de errores más avanzado con raise, try/except y teniendo una jerarquía de excepciones usando subclases de Exception para poder tener custom exceptions, además de practicar cómo se documenta un proyecto más completo, se puede notar en el código que hay una documentación bastante detallada, quizás no perfecta o quizás sobrecargada pero lo suficiente para entender qué hace cada cosa.

Puntos a reforzar según el código de E27
Protocolo y Semántica de Métodos Mágicos (Dunder Methods)

El fallo: En __eq__, lanzaste una excepción cuando la clase no coincidía y usaste pass en la comparación, lo que terminó devolviendo True incondicionalmente.

La regla: Los métodos especiales de comparación (__eq__, __lt__, etc.) deben devolver únicamente un valor booleano (True o False). Si el objeto comparado no pertenece a la clase o sus atributos no coinciden, se retorna False sin romper el flujo con excepciones.

Alcance de Variables y Flujo en Menús Extensos (main.py)

El fallo: Olvidaste definir simbolo en la opción de bonos y confundiste agregar_activo con comprar_activo dentro de un case.

La causa: Al escribir scripts principales con match/case y menús anidados de muchas líneas, es fácil perder la trazabilidad de las variables locales.

La solución: Mantener bloques de lógica pequeños. Si un case supera las 10-15 líneas solicitando datos por consola, es señal de que esa recolección de datos debe aislarse en una función auxiliar (ej. solicitar_datos_activo()).

Semántica de Setters (@property.setter) vs Métodos Explicitos

El concepto: Los setters en Python representan la operación de asignación =. Hacer una suma acumulativa (self._saldo += valor) dentro de un setter rompe la expectativa de cómo funciona una propiedad. Si vas a mutar un valor acumulándolo, usa un método con un verbo claro como depositar_saldo(monto).

Uso correcto de Docstrings vs Comentarios Inline

El concepto: Las cadenas triples """...""" al inicio de un módulo, clase o función son procesadas por Python como la documentación oficial (docstring). No deben usarse como comentarios explicativos dentro del cuerpo de un if, while o match/case; para eso existen los comentarios tradicionales con #.