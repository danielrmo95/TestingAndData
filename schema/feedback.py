from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Comentario(BaseModel):
    curso_id: int                  # ID del curso al que pertenece el comentario
    entidad_id: int                # ID de la entidad que realiza el comentario
    comentario: str                     # Texto del comentario
    fecha_comentario: Optional[datetime] = Field(None, description="Fecha de registro en formato ISO")  # Fecha del comentario, opcional al crear un nuevo registro

class ComentarioResponse(BaseModel):
    comentario_id: int             # ID del comentario
    curso_id: int                  # ID del curso asociado
    entidad_id: int                # ID de la entidad que hizo el comentario
    comentario: str                     # Texto del comentario
    fecha_comentario: str          # Fecha del comentario como string (puedes ajustar a Date si es necesario)
