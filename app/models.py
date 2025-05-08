from pydantic import BaseModel, EmailStr
from typing import List

class ServicioRegistro(BaseModel):
    nombre: str
    descripcion: str
    endpoints: List[str]

class UsuarioLogin(BaseModel):
    nombre_usuario: str
    contrasena: str

class Orquestacion(BaseModel):
    servicio_destino: str
    parametros_adicionales: dict

class ReglasActualizacion(BaseModel):
    reglas: dict

class AutorizacionAcceso(BaseModel):
    recursos: List[str]
    rol_usuario: str
