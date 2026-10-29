"""Operaciones y almacenamiento local de tareas."""

import json

from config.settings import DATA_DIR, TASKS_FILE
from src.models.tarea import Tarea


def listar_tareas() -> list[Tarea]:
    if not TASKS_FILE.exists():
        return []
    try:
        datos = json.loads(TASKS_FILE.read_text(encoding="utf-8"))
        return [Tarea.desde_dict(item) for item in datos]
    except (json.JSONDecodeError, TypeError, KeyError):
        return []


def _guardar(tareas: list[Tarea]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    contenido = [tarea.a_dict() for tarea in tareas]
    TASKS_FILE.write_text(
        json.dumps(contenido, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def agregar_tarea(titulo: str) -> None:
    tareas = listar_tareas()
    tareas.append(Tarea(titulo=titulo))
    _guardar(tareas)


def completar_tarea(indice: int) -> bool:
    tareas = listar_tareas()
    if indice < 0 or indice >= len(tareas):
        return False
    tareas[indice].completada = True
    _guardar(tareas)
    return True
