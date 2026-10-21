import logging

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.schemas import NotificarTelegramRequest, NotificarTelegramResponse
from app.RN.telegram_rn import TelegramRN

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api",
    tags=["Notificaciones"],
)


@router.post(
    "/notificarTelegram",
    response_model=NotificarTelegramResponse,
    status_code=status.HTTP_200_OK,
    summary="Enviar notificación por Telegram",
    description="Recibe un texto y envía una notificación por Telegram.",
)
async def notificar_telegram(
    payload: NotificarTelegramRequest,
) -> NotificarTelegramResponse:
    """Procesa una solicitud de notificación por Telegram.

    Delega la lógica de envío a la capa de reglas de negocio (TelegramRN).
    """
    logger.info("Notificación Telegram recibida — texto: %s", payload.texto)

    telegram_rn = TelegramRN()
    try:
        await telegram_rn.Enviar(payload)
    except Exception as e:
        logger.error("Error al procesar notificación: %s", str(e))
        return JSONResponse(
            status_code=status.HTTP_502_BAD_GATEWAY,
            content={
                "status": "error",
                "mensaje": f"No se pudo enviar el mensaje por Telegram: {str(e)}",
            },
        )

    return NotificarTelegramResponse(
        status="ok",
        mensaje="Notificación procesada correctamente",
    )
