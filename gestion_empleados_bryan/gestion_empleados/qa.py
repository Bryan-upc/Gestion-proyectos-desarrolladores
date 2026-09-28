"""
Clase QA (Quality Assurance / control de calidad).

Hereda de Empleado. Su costo por hora depende de un costo base más un
bono por cada certificación que tenga.
"""

from empleado import Empleado
from excepciones import DatosInvalidosError


class QA(Empleado):

    COSTO_BASE = 30.0
    BONO_POR_CERTIFICACION = 5.0

    def __init__(self, id_empleado, nombres, apellidos, email,
                 certificaciones=0, horas_trabajadas=0):
        super().__init__(id_empleado, nombres, apellidos, email, horas_trabajadas)

        if not isinstance(certificaciones, int) or certificaciones < 0:
            raise DatosInvalidosError("El número de certificaciones no puede ser negativo.")

        self.__certificaciones = certificaciones

    def obtener_certificaciones(self):
        return self.__certificaciones

    def calcular_costo_hora(self):
        # POLIMORFISMO: fórmula distinta a la de Desarrollador y LiderTecnico
        return self.COSTO_BASE + (self.__certificaciones * self.BONO_POR_CERTIFICACION)

    def obtener_tipo(self):
        return "QA"
