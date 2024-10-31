from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class EntidadEducativa(BaseModel):
    nombre: str                # Nombre de la entidad educativa
    email: str                 # Correo electrónico de la entidad
    contrasena: str          # Contraseña para la entidad educativa
    nombre_representante: str   # Nombre del representante
    telefono_representante: Optional[str]  # Teléfono del representante, puede ser opcional
    fecha_registro: Optional[datetime] = Field(None, description="Fecha de registro en formato ISO")

class EntidadEducativaResponse(BaseModel):
    entidad_id: int
    nombre: str
    email: str
    nombre_representante: str
    telefono_representante: Optional[str]
    fecha_registro: Optional[str]  # Mantener esto como string