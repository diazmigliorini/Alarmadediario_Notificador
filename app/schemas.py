from pydantic import BaseModel, Field, field_validator


class NotificarTelegramRequest(BaseModel):
    """Esquema de entrada para el endpoint notificarTelegram."""

    texto: str = Field(
        ...,
        min_length=1,
        description="Texto del mensaje a enviar por Telegram",
        examples=["Aquí va el texto del mensaje"],
    )

    @field_validator("texto", mode="before")
    @classmethod
    def texto_no_vacio(cls, v: str) -> str:
        """Elimina espacios extremos y rechaza textos vacíos."""
        if isinstance(v, str):
            v = v.strip()
        if not v:
            raise ValueError("El texto no puede estar vacío")
        return v


class NotificarTelegramResponse(BaseModel):
    """Esquema de respuesta para el endpoint notificarTelegram."""

    status: str = Field(
        default="ok",
        description="Estado de la operación",
    )
    mensaje: str = Field(
        default="Notificación procesada correctamente",
        description="Mensaje descriptivo del resultado",
    )
