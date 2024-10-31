from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    nombre_curso: str
    descripcion: Optional[str]
    instructor: str          
    entidad_id: int           

class CursoResponse(BaseModel):
    curso_id: int
    nombre_curso: str
    descripcion: Optional[str]
    instructor: str
    entidad_id: int