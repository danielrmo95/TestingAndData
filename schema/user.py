from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] 
    Nombre: str 
    Edad: int  
    CorreoElectronico: str

class UserResponse(BaseModel):
    id: int
    Nombre: str 
    Edad: int 
    CorreoElectronico: str

    