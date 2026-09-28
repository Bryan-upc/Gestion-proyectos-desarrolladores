"""
Clase Desarrollador.

Hereda de Empleado y define su propia forma de calcular el costo por
hora, según su nivel (junior, semi senior, senior).
"""

from empleado import Empleado
from excepciones import DatosInvalidosError


class Desarrollador(Empleado):

    # Diccionario con el costo por hora según el nivel (regla de negocio)
    COSTO_POR_NIVEL = {
        "junior": 25.0,
        "semi senior": 40.0,
        "senior": 60.0,
    }

    def __init__(self, id_empleado, nombres, apellidos, email,
                 nivel, lenguaje_principal, horas_trabajadas=0):
        # Llama al constructor de la clase padre (Empleado)
        super().__init__(id_empleado, nombres, apellidos, email, horas_trabajadas)

        nivel = self._validar_texto(nivel, "Nivel").lower()
        if nivel not in self.COSTO_POR_NIVEL:
            opciones = list(self.COSTO_POR_NIVEL.keys())
            raise DatosInvalidosError(f"Nivel '{nivel}' no válido. Opciones: {opciones}")

        self.__nivel = nivel
        self.__lenguaje_principal = self._validar_texto(lenguaje_principal, "Lenguaje principal")

    def obtener_nivel(self):
        return self.__nivel

    def obtener_lenguaje_principal(self):
        return self.__lenguaje_principal

    def calcular_costo_hora(self):
        # POLIMORFISMO: esta versión es distinta a la de QA y LiderTecnico
        return self.COSTO_POR_NIVEL[self.__nivel]

    def obtener_tipo(self):
        return "Desarrollador"
