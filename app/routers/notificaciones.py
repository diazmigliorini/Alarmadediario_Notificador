import logging

from fastapi import APIRouter, status

from app.schemas import NotificarTelegramRequest, NotificarTelegramResponse

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
    description="Recibe un texto y simula el envío de una notificación por Telegram.",
)
async def notificar_telegram(
    payload: NotificarTelegramRequest,
) -> NotificarTelegramResponse:
    """Procesa una solicitud de notificación por Telegram.

    Por ahora, la lógica simula el envío registrando el texto recibido en el log.
    En una implementación futura se integrará con la API de Telegram Bot.
    """
    logger.info("Notificación Telegram recibida — texto: %s", payload.texto)

    # TODO: Aquí irá la lógica real de envío a Telegram (Bot API).
    # Ejemplo futuro:
    #   await telegram_service.send_message(chat_id=CHAT_ID, text=payload.texto)

    return NotificarTelegramResponse(
        status="ok",
        mensaje="Notificación procesada correctamente",
    )
