"""Regla de negocio para notificaciones de Telegram."""

import logging

from app.schemas import NotificarTelegramRequest
from app.Servicios.telegram_servicio import TelegramServicio

logger = logging.getLogger(__name__)


class TelegramRN:
    """Encapsula la lógica de negocio para el envío de notificaciones por Telegram."""

    async def Enviar(self, mensaje: NotificarTelegramRequest) -> None:
        """Procesa y envía la notificación recibida desde la API.

        Parámetros
        ----------
        mensaje : NotificarTelegramRequest
            El payload completo recibido en el endpoint.
        """
        logger.info("TelegramRN.Enviar — texto: %s", mensaje.texto)

        servicio = TelegramServicio()
        await servicio.Enviar(mensaje)
