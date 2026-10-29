"""Configuración central del proyecto."""

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
TASKS_FILE = DATA_DIR / "tareas.json"
APP_NAME = "Lista de tareas"
