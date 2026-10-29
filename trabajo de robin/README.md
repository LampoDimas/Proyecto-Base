# Proyecto base de informática

Plantilla inicial de una aplicación de consola en Python. El ejemplo implementa una pequeña lista de tareas y separa la entrada del usuario, las reglas de negocio, los modelos y la configuración.

## Requisitos

- Python 3.10 o superior

## Ejecutar

Desde la carpeta raíz del proyecto:

```powershell
python -m src.main
```

El programa muestra un menú para listar, agregar y completar tareas. Los datos se guardan en `data/tareas.json`.

## Estructura

```text
proyecto-base/
├── config/
│   └── settings.py       # Configuración general
├── data/
│   └── .gitkeep          # Carpeta para datos locales
├── docs/
│   └── estructura.md     # Descripción de carpetas y módulos
├── src/
│   ├── __init__.py
│   ├── main.py           # Inicio de la aplicación
│   ├── models/
│   │   ├── __init__.py
│   │   └── tarea.py      # Modelo de tarea
│   └── services/
│       ├── __init__.py
│       └── tareas.py     # Operaciones y persistencia
├── .gitignore
├── pyproject.toml        # Metadatos y configuración del proyecto
└── README.md
```

## Publicar en GitHub

1. Crea un repositorio vacío llamado `proyecto-base` en GitHub.
2. En esta carpeta ejecuta:

   ```powershell
   git remote add origin https://github.com/TU-USUARIO/proyecto-base.git
   git branch -M main
   git push -u origin main
   ```

3. Desde esta carpeta, agrega y envía los archivos:

   ```powershell
   git add .
   git commit -m "Crear estructura base del proyecto"
   git remote add origin https://github.com/TU-USUARIO/proyecto-base.git
   git push -u origin main
   ```

4. Abre la página del repositorio y toma una captura donde se vea el nombre del repositorio y los archivos. Adjunta esa captura en la entrega de la plataforma.

Cambia `TU-USUARIO` por tu usuario real de GitHub.
