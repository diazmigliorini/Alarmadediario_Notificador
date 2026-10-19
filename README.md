# Alarmadediario Notificador

Web API para enviar notificaciones a través de Telegram.

## Requisitos

- Python 3.10+

## Instalación

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Levantar el servidor

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

El servidor quedará disponible en `http://localhost:8000`.

## Documentación interactiva

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
