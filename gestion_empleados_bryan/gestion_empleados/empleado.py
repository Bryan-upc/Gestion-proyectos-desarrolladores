"""
Clase Empleado (clase abstracta / clase base).

Representa los datos y comportamientos que TODOS los empleados de la
consultora tienen en común. No se puede crear un objeto Empleado
directamente; se debe usar una de sus subclases: Desarrollador, QA o
LiderTecnico (esto es HERENCIA).

El método calcular_costo_hora() no tiene una implementación aquí: cada
subclase lo define a su manera. Esto es POLIMORFISMO: el mismo método
"calcular_costo_hora" se comporta distinto según el tipo de empleado.
"""

from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError


class Empleado(ABC):

    def __init__(self, id_empleado, nombres, apellidos, email, horas_trabajadas=0):
        # Atributos con doble guion bajo -> ENCAPSULAMIENTO.
        # No se puede acceder desde fuera como objeto.__nombres, solo
        # a través de los métodos "obtener_..." que se definen más abajo.
        self.__id_empleado = self._validar_texto(id_empleado, "ID")
        self.__nombres = self._validar_texto(nombres, "Nombres")
        self.__apellidos = self._validar_texto(apellidos, "Apellidos")
        self.__email = self._validar_email(email)
        self.__horas_trabajadas = self._validar_horas(horas_trabajadas)

    # ------------------------------------------------------------------
    # Validaciones reutilizables por las subclases (control de excepciones)
    # Usan un solo guion bajo para poder ser usadas por Desarrollador,
    # QA y LiderTecnico.
    # ------------------------------------------------------------------
    def _validar_texto(self, valor, nombre_campo):
        if not isinstance(valor, str) or valor.strip() == "":
            raise DatosInvalidosError(f"{nombre_campo} no puede estar vacío.")
        return valor.strip()

    def _validar_email(self, email):
        if not isinstance(email, str) or "@" not in email or "." not in email:
            raise DatosInvalidosError(f"El email '{email}' no tiene un formato válido.")
        return email.strip()

    def _validar_horas(self, horas):
        if not isinstance(horas, (int, float)) or horas < 0:
            raise DatosInvalidosError("Las horas trabajadas no pueden ser negativas.")
        return horas

    # ------------------------------------------------------------------
    # Getters (forma correcta de leer los atributos privados)
    # ------------------------------------------------------------------
    def obtener_id(self):
        return self.__id_empleado

    def obtener_nombres(self):
        return self.__nombres

    def obtener_apellidos(self):
        return self.__apellidos

    def obtener_nombre_completo(self):
        return f"{self.__nombres} {self.__apellidos}"

    def obtener_email(self):
        return self.__email

    def obtener_horas_trabajadas(self):
        return self.__horas_trabajadas

    # ------------------------------------------------------------------
    # Comportamiento común
    # ------------------------------------------------------------------
    def registrar_horas(self, horas):
        """Suma horas trabajadas al acumulado del empleado."""
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise DatosInvalidosError("Las horas a registrar deben ser un número mayor a 0.")
        self.__horas_trabajadas += horas

    @abstractmethod
    def calcular_costo_hora(self):
        """
        Cada subclase debe indicar cuánto cuesta 1 hora de ese empleado.
        (Método abstracto: obliga a que Desarrollador, QA y LiderTecnico
        lo implementen).
        """
        pass

    @abstractmethod
    def obtener_tipo(self):
        """Devuelve el tipo de empleado como texto: 'Desarrollador', 'QA', etc."""
        pass

    def calcular_costo_total(self):
        """Costo total generado por el empleado = costo por hora x horas trabajadas."""
        return self.calcular_costo_hora() * self.__horas_trabajadas

    def __str__(self):
        return (
            f"[{self.obtener_tipo()}] {self.__id_empleado} - {self.obtener_nombre_completo()} "
            f"| Email: {self.__email} | Horas: {self.__horas_trabajadas} "
            f"| Costo x hora: S/ {self.calcular_costo_hora():.2f} "
            f"| Costo total: S/ {self.calcular_costo_total():.2f}"
        )
