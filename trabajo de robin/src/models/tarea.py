"""Modelo de una tarea."""

from dataclasses import asdict, dataclass


@dataclass
class Tarea:
    titulo: str
    completada: bool = False

    def a_dict(self) -> dict[str, str | bool]:
        return asdict(self)

    @classmethod
    def desde_dict(cls, datos: dict[str, str | bool]) -> "Tarea":
        return cls(
            titulo=str(datos["titulo"]),
            completada=bool(datos.get("completada", False)),
        )
