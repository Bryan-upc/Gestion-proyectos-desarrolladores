"""
Excepciones personalizadas para el módulo de Gestión de Empleados.

Se crean clases de excepción propias (heredan de Exception) para poder
identificar con claridad qué tipo de error ocurrió, en lugar de usar
siempre errores genéricos de Python.
"""


class DatosInvalidosError(Exception):
    """Se lanza cuando algún dato ingresado no cumple las validaciones."""
    pass


class EmpleadoNoEncontradoError(Exception):
    """Se lanza cuando se busca un empleado por ID y no existe."""
    pass


class EmpleadoDuplicadoError(Exception):
    """Se lanza cuando se intenta registrar un ID de empleado que ya existe."""
    pass
