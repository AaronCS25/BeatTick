# BeatTick

Backend inicial en Python basado en FastAPI y SQLModel, con una arquitectura basada en features.

## Estructura del Proyecto

El proyecto sigue una arquitectura basada en features, donde cada funcionalidad principal de la aplicación se encuentra en su propio directorio dentro de `app/features`.

- **`app/`**: Directorio principal de la aplicación.
  - **`main.py`**: Punto de entrada de la aplicación FastAPI.
  - **`database.py`**: Configuración de la base de datos SQLite.
  - **`features/`**: Contiene las diferentes features de la aplicación.
    - **`items/`**: Feature de ejemplo para gestionar "ítems".
      - `models.py`: Modelos de la base de datos (SQLModel).
      - `schemas.py`: Esquemas de validación (Pydantic).
      - `services.py`: Lógica de negocio.
      - `router.py`: Endpoints de la API (FastAPI Router).
- **`requirements.txt`**: Dependencias del proyecto.

## Cómo Empezar

### Prerrequisitos

- Python 3.9+
- pip

### Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_DIRECTORIO>
   ```

2. (Opcional pero recomendado) Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   # En Windows
   .venv\Scripts\activate
   # En macOS/Linux
   source .venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

Para iniciar el servidor de desarrollo, ejecuta el siguiente comando en la raíz del proyecto:

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en `http://127.0.0.1:8000`.

### Documentación de la API

Una vez que el servidor esté en funcionamiento, puedes acceder a la documentación interactiva de la API (generada por Swagger UI) en:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Desde allí, podrás ver todos los endpoints disponibles y probarlos directamente.