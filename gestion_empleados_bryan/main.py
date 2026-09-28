"""
main.py

Demo de consola del módulo "Gestión de Empleados" (rama feature/gestion-empleados).

Este archivo NO es el menú principal del sistema completo (eso lo hace
Jose Luis en su clase MenuPrincipal). Este es un pequeño menú para
poder probar el módulo de forma independiente en Visual Studio Code
mientras se desarrolla, y para mostrarlo al equipo.

Para ejecutar: abrir esta carpeta en VS Code y correr este archivo
(botón "Run" o F5), o desde la terminal: python main.py
"""

import sys
import os

# Permite importar las clases desde la carpeta gestion_empleados
sys.path.append(os.path.join(os.path.dirname(__file__), "gestion_empleados"))

from gestor_empleados import GestorEmpleados
from desarrollador import Desarrollador
from qa import QA
from lider_tecnico import LiderTecnico
from excepciones import DatosInvalidosError, EmpleadoNoEncontradoError, EmpleadoDuplicadoError


def cargar_datos_iniciales(gestor):
    """Registra algunos empleados de ejemplo para no empezar con la lista vacía."""
    gestor.registrar_empleado(
        Desarrollador("E001", "Bryan", "Villagomez", "bryan@NTTData.com",
                       nivel="senior", lenguaje_principal="Python", horas_trabajadas=8)
    )
    gestor.registrar_empleado(
        QA("E002", "Fabiola", "Valverde", "fabiola@NTTData.com",
           certificaciones=2, horas_trabajadas=8)
    )
    gestor.registrar_empleado(
        LiderTecnico("E003", "Osmar", "Mosquera", "osmar@NTTData.com",
                      anios_experiencia=5, horas_trabajadas=9)
    )
    gestor.registrar_empleado(
        LiderTecnico("E004", "Jose", "Pintado", "jose@NTTData.com",
                      anios_experiencia=5, horas_trabajadas=12)
    )

def menu():
    gestor = GestorEmpleados()
    cargar_datos_iniciales(gestor)

    opcion = ""
    while opcion != "0":
        print("\n--- MODULO: GESTION DE EMPLEADOS ---")
        print("1. Registrar Desarrollador")
        print("2. Registrar QA")
        print("3. Registrar Lider Tecnico")
        print("4. Buscar empleado por ID")
        print("5. Listar todos los empleados")
        print("6. Registrar horas trabajadas a un empleado")
        print("7. Ver costo total del equipo")
        print("0. Salir")
        opcion = input("Elige una opcion: ").strip()

        try:
            if opcion == "1":
                id_e = input("ID: ")
                nombres = input("Nombres: ")
                apellidos = input("Apellidos: ")
                email = input("Email: ")
                nivel = input("Nivel (junior / semi senior / senior): ")
                lenguaje = input("Lenguaje principal: ")
                gestor.registrar_empleado(
                    Desarrollador(id_e, nombres, apellidos, email, nivel, lenguaje)
                )
                print("Desarrollador registrado correctamente.")

            elif opcion == "2":
                id_e = input("ID: ")
                nombres = input("Nombres: ")
                apellidos = input("Apellidos: ")
                email = input("Email: ")
                certificaciones = int(input("Cantidad de certificaciones: "))
                gestor.registrar_empleado(
                    QA(id_e, nombres, apellidos, email, certificaciones)
                )
                print("QA registrado correctamente.")

            elif opcion == "3":
                id_e = input("ID: ")
                nombres = input("Nombres: ")
                apellidos = input("Apellidos: ")
                email = input("Email: ")
                anios = float(input("Años de experiencia: "))
                gestor.registrar_empleado(
                    LiderTecnico(id_e, nombres, apellidos, email, anios)
                )
                print("Lider Tecnico registrado correctamente.")

            elif opcion == "4":
                id_e = input("ID a buscar: ")
                empleado = gestor.buscar_empleado(id_e)
                print(empleado)

            elif opcion == "5":
                empleados = gestor.listar_empleados()
                if not empleados:
                    print("No hay empleados registrados.")
                for empleado in empleados:
                    print(empleado)

            elif opcion == "6":
                id_e = input("ID del empleado: ")
                horas = float(input("Horas a registrar: "))
                empleado = gestor.buscar_empleado(id_e)
                empleado.registrar_horas(horas)
                print("Horas registradas correctamente.")

            elif opcion == "7":
                total = gestor.calcular_costo_total_equipo()
                print(f"Costo total del equipo: S/ {total:.2f}")

            elif opcion == "0":
                print("Saliendo del modulo...")

            else:
                print("Opcion no valida.")

        # Control de excepciones: en vez de que el programa se caiga,
        # se muestra un mensaje claro y el menu sigue funcionando.
        except DatosInvalidosError as error:
            print(f"Dato invalido: {error}")
        except EmpleadoNoEncontradoError as error:
            print(f"No encontrado: {error}")
        except EmpleadoDuplicadoError as error:
            print(f"Duplicado: {error}")
        except ValueError:
            print("Debes ingresar un numero valido.")


if __name__ == "__main__":
    menu()
