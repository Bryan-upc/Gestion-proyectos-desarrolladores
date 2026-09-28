"""
pruebas.py

Pruebas simples (con "assert") de los métodos del módulo de Gestión
de Empleados. Se usan asserts en vez de un framework como unittest
para que sea fácil de leer y ejecutar.

Ejecutar en VS Code (Run) o por terminal: python pruebas.py
Si todo está bien, al final se imprime "TODAS LAS PRUEBAS PASARON".
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "gestion_empleados"))

from gestor_empleados import GestorEmpleados
from desarrollador import Desarrollador
from qa import QA
from lider_tecnico import LiderTecnico
from excepciones import DatosInvalidosError, EmpleadoNoEncontradoError, EmpleadoDuplicadoError


def prueba_creacion_y_costo_por_hora():
    dev = Desarrollador("D1", "Bryan", "Villagomez", "bryan@NTTData.com", "senior", "Python")
    qa = QA("Q1", "Ana", "Torres", "ana@NTTData.com", certificaciones=2)
    lider = LiderTecnico("L1", "Jose", "Pintado", "luis@NTTData.com", anios_experiencia=5)

    # Polimorfismo: mismo método, resultados distintos según el tipo
    assert dev.calcular_costo_hora() == 60.0
    assert qa.calcular_costo_hora() == 30.0 + 2 * 5.0
    assert lider.calcular_costo_hora() == 70.0 + 5 * 3.0
    print("OK - prueba_creacion_y_costo_por_hora")


def prueba_registrar_horas_y_costo_total():
    dev = Desarrollador("D2", "Carlos", "Ruiz", "carlos@NTTData.com", "junior", "Java")
    dev.registrar_horas(10)
    dev.registrar_horas(5)
    assert dev.obtener_horas_trabajadas() == 15
    assert dev.calcular_costo_total() == 25.0 * 15
    print("OK - prueba_registrar_horas_y_costo_total")


def prueba_gestor_registrar_y_buscar():
    gestor = GestorEmpleados()
    dev = Desarrollador("D3", "Sofia", "Leon", "sofia@NTTData.com", "semi senior", "C#")
    gestor.registrar_empleado(dev)

    encontrado = gestor.buscar_empleado("D3")
    assert encontrado.obtener_nombre_completo() == "Sofia Leon"
    assert gestor.cantidad_empleados() == 1
    print("OK - prueba_gestor_registrar_y_buscar")


def prueba_gestor_listar_por_tipo():
    gestor = GestorEmpleados()
    gestor.registrar_empleado(Desarrollador("D4", "A", "A", "a@NTTData.com", "junior", "Python"))
    gestor.registrar_empleado(QA("Q2", "B", "B", "b@NTTData.com", certificaciones=1))
    gestor.registrar_empleado(LiderTecnico("L2", "C", "C", "c@NTTData.com", anios_experiencia=2))

    assert len(gestor.listar_por_tipo("Desarrollador")) == 1
    assert len(gestor.listar_por_tipo("QA")) == 1
    assert len(gestor.listar_por_tipo("Lider Tecnico")) == 1
    assert len(gestor.listar_empleados()) == 3
    print("OK - prueba_gestor_listar_por_tipo")


def prueba_costo_total_equipo():
    gestor = GestorEmpleados()
    dev = Desarrollador("D5", "A", "A", "a@NTTData.com", "junior", "Python")  # 25/h
    dev.registrar_horas(2)  # 50
    qa = QA("Q3", "B", "B", "b@NTTData.com", certificaciones=0)  # 30/h
    qa.registrar_horas(1)  # 30
    gestor.registrar_empleado(dev)
    gestor.registrar_empleado(qa)

    assert gestor.calcular_costo_total_equipo() == 80.0
    print("OK - prueba_costo_total_equipo")


def prueba_excepcion_datos_invalidos():
    try:
        Desarrollador("D6", "", "Perez", "correo_invalido", "junior", "Python")
        assert False, "Debio lanzar DatosInvalidosError por nombre vacio"
    except DatosInvalidosError:
        pass

    try:
        Desarrollador("D7", "Juan", "Perez", "juan-arroba-mal.com", "junior", "Python")
        assert False, "Debio lanzar DatosInvalidosError por email invalido"
    except DatosInvalidosError:
        pass

    try:
        Desarrollador("D8", "Juan", "Perez", "juan@mail.com", "nivel_inventado", "Python")
        assert False, "Debio lanzar DatosInvalidosError por nivel invalido"
    except DatosInvalidosError:
        pass

    print("OK - prueba_excepcion_datos_invalidos")


def prueba_excepcion_empleado_no_encontrado():
    gestor = GestorEmpleados()
    try:
        gestor.buscar_empleado("NO_EXISTE")
        assert False, "Debio lanzar EmpleadoNoEncontradoError"
    except EmpleadoNoEncontradoError:
        pass
    print("OK - prueba_excepcion_empleado_no_encontrado")


def prueba_excepcion_empleado_duplicado():
    gestor = GestorEmpleados()
    gestor.registrar_empleado(Desarrollador("D9", "A", "A", "a@mail.com", "junior", "Python"))
    try:
        gestor.registrar_empleado(Desarrollador("D9", "B", "B", "b@mail.com", "junior", "Python"))
        assert False, "Debio lanzar EmpleadoDuplicadoError"
    except EmpleadoDuplicadoError:
        pass
    print("OK - prueba_excepcion_empleado_duplicado")


if __name__ == "__main__":
    prueba_creacion_y_costo_por_hora()
    prueba_registrar_horas_y_costo_total()
    prueba_gestor_registrar_y_buscar()
    prueba_gestor_listar_por_tipo()
    prueba_costo_total_equipo()
    prueba_excepcion_datos_invalidos()
    prueba_excepcion_empleado_no_encontrado()
    prueba_excepcion_empleado_duplicado()
    print("\nTODAS LAS PRUEBAS PASARON")
