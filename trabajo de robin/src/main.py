"""Punto de entrada de la aplicación."""

from config.settings import APP_NAME
from src.services.tareas import agregar_tarea, completar_tarea, listar_tareas


def mostrar_menu() -> None:
    print(f"\n=== {APP_NAME} ===")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("0. Salir")


def ejecutar() -> None:
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            tareas = listar_tareas()
            if not tareas:
                print("Todavía no hay tareas.")
            for numero, tarea in enumerate(tareas, start=1):
                estado = "✓" if tarea.completada else " "
                print(f"{numero}. [{estado}] {tarea.titulo}")
        elif opcion == "2":
            titulo = input("Título de la tarea: ").strip()
            if titulo:
                agregar_tarea(titulo)
                print("Tarea agregada.")
            else:
                print("El título no puede estar vacío.")
        elif opcion == "3":
            try:
                numero = int(input("Número de tarea: "))
                if completar_tarea(numero - 1):
                    print("Tarea completada.")
                else:
                    print("No existe una tarea con ese número.")
            except ValueError:
                print("Escribe un número válido.")
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar()
