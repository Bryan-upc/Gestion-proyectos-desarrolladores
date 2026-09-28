"""
Clase LiderTecnico.

Hereda de Empleado. Su costo por hora depende de un costo base más un
bono por cada año de experiencia.
"""

from empleado import Empleado
from excepciones import DatosInvalidosError


class LiderTecnico(Empleado):

    COSTO_BASE = 70.0
    BONO_POR_ANIO_EXPERIENCIA = 3.0

    def __init__(self, id_empleado, nombres, apellidos, email,
                 anios_experiencia, horas_trabajadas=0):
        super().__init__(id_empleado, nombres, apellidos, email, horas_trabajadas)

        if not isinstance(anios_experiencia, (int, float)) or anios_experiencia < 0:
            raise DatosInvalidosError("Los años de experiencia no pueden ser negativos.")

        self.__anios_experiencia = anios_experiencia

    def obtener_anios_experiencia(self):
        return self.__anios_experiencia

    def calcular_costo_hora(self):
        # POLIMORFISMO: fórmula distinta a la de Desarrollador y QA
        return self.COSTO_BASE + (self.__anios_experiencia * self.BONO_POR_ANIO_EXPERIENCIA)

    def obtener_tipo(self):
        return "Lider Tecnico"
