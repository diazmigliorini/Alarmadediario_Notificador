"""Servicio para el envío de mensajes a través de la API de Telegram Bot."""

import logging
import os

from telegram import Bot

from app.schemas import NotificarTelegramRequest

logger = logging.getLogger(__name__)


class TelegramServicio:
    """Gestiona la comunicación directa con la API de Telegram Bot."""

    def __init__(self) -> None:
        """Inicializa el bot con las credenciales del entorno."""
        self._token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
        self._chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()

        if not self._token or not self._chat_id:
            logger.error("Credenciales de Telegram no configuradas en el entorno (.env)")

        self._bot = Bot(token=self._token) if self._token else None

    async def Enviar(self, mensaje: NotificarTelegramRequest) -> None:
        """Envía el mensaje a Telegram.

        Parámetros
        ----------
        mensaje : NotificarTelegramRequest
            El payload con el texto a enviar.
        """
        if not self._bot or not self._chat_id:
            raise RuntimeError("Telegram no está configurado correctamente (faltan variables en .env)")

        logger.info("TelegramServicio.Enviar — texto: %s", mensaje.texto)

        try:
            await self._bot.send_message(
                chat_id=self._chat_id,
                text=mensaje.texto,
            )
            logger.info("Mensaje enviado a Telegram correctamente.")
        except Exception as e:
            logger.error("Error al enviar mensaje a Telegram: %s", str(e))
            raise

