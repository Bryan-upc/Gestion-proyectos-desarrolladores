"""
Clase GestorEmpleados.

Administra la colección (lista) de empleados: registrar, buscar,
listar y calcular costos del equipo completo. Esta clase NO hereda de
Empleado, simplemente lo usa (tiene una lista de objetos Empleado).
"""

from excepciones import EmpleadoNoEncontradoError, EmpleadoDuplicadoError


class GestorEmpleados:

    def __init__(self):
        self.__empleados = []  # Lista (colección) de objetos Empleado

    def registrar_empleado(self, empleado):
        """Agrega un empleado a la lista, validando que el ID no exista ya."""
        if self.buscar_empleado(empleado.obtener_id(), lanzar_error=False) is not None:
            raise EmpleadoDuplicadoError(
                f"Ya existe un empleado registrado con el ID '{empleado.obtener_id()}'."
            )
        self.__empleados.append(empleado)

    def buscar_empleado(self, id_empleado, lanzar_error=True):
        """Busca un empleado por su ID recorriendo la lista."""
        for empleado in self.__empleados:
            if empleado.obtener_id() == id_empleado:
                return empleado

        if lanzar_error:
            raise EmpleadoNoEncontradoError(f"No se encontró ningún empleado con ID '{id_empleado}'.")
        return None

    def listar_empleados(self):
        """Devuelve una copia de la lista completa de empleados."""
        return list(self.__empleados)

    def listar_por_tipo(self, tipo):
        """Filtra la lista de empleados por tipo: 'Desarrollador', 'QA' o 'Lider Tecnico'."""
        return [e for e in self.__empleados if e.obtener_tipo().lower() == tipo.lower()]

    def calcular_costo_total_equipo(self):
        """Suma el costo total (costo/hora x horas) de todos los empleados registrados."""
        return sum(empleado.calcular_costo_total() for empleado in self.__empleados)

    def cantidad_empleados(self):
        return len(self.__empleados)
