"""Alarmadediario Notificador — Web API.

Punto de entrada de la aplicación FastAPI.
"""

import logging

from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.routers import notificaciones

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
)

# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Alarmadediario Notificador",
    description="API para enviar notificaciones a través de Telegram.",
    version="0.1.0",
)


# ---------------------------------------------------------------------------
# Manejo global de errores de validación
# ---------------------------------------------------------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    """Devuelve errores de validación en el formato estándar de la API."""
    errores = []
    for error in exc.errors():
        campo = " -> ".join(str(loc) for loc in error["loc"] if loc != "body")
        errores.append(f"{campo}: {error['msg']}")

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "status": "error",
            "mensaje": "; ".join(errores),
        },
    )


# Registrar routers
app.include_router(notificaciones.router)


@app.get("/", tags=["Health"])
async def health_check() -> dict:
    """Verificación básica de que el servicio está activo."""
    return {"status": "ok", "servicio": "Alarmadediario Notificador"}
