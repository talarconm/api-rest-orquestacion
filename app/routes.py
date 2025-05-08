from fastapi import APIRouter, HTTPException, Depends
from app.models import *

router = APIRouter()


@router.get("/") # type: ignore
## Definimos la funcion a ejecutar en la ruta `localhost:<puerto>/`
### PYTHONTIP: El guion bajo o _underscore_ tiene varios roles en Python ([text](https://www.geeksforgeeks.org/underscore-_-python/))
### En este caso, lo usamos para definir una funcion cuyo nombre no es relevante
def _():
## El cuerpo de nuestra funcion solo retorna un diccionario, con un mensaje
    return {
        "message": "Hello World from my first API",
    }

# Simulación de token y roles
TOKEN_VALIDO = "123456"
USUARIOS = {
    "admin": {"rol": "Administrador"},
    "orquestador": {"rol": "Orquestador"}
}

def validar_token(token: str):
    if token != TOKEN_VALIDO:
        raise HTTPException(status_code=401, detail="Token inválido")

@router.post("/autenticar-usuario")
def autenticar_usuario(usuario: UsuarioLogin):
    return {"token": TOKEN_VALIDO, "rol": "Administrador"}

@router.post("/autorizar-acceso")
def autorizar_acceso(data: AutorizacionAcceso):
    if data.rol_usuario not in ["Administrador", "Orquestador"]:
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return {"acceso": "Autorizado"}

@router.post("/orquestar")
def orquestar_servicio(data: Orquestacion, token: str = Depends(validar_token)):
    return {"mensaje": f"Orquestando servicio {data.servicio_destino}"}

@router.get("/informacion-servicio/{id}")
def obtener_servicio(id: str, token: str = Depends(validar_token)):
    return {"id": id, "descripcion": "Servicio de prueba"}

@router.post("/registrar-servicio")
def registrar_servicio(data: ServicioRegistro, token: str = Depends(validar_token)):
    return {"mensaje": f"Servicio {data.nombre} registrado"}

@router.put("/actualizar-reglas-orquestacion")
def actualizar_reglas(data: ReglasActualizacion, token: str = Depends(validar_token)):
    return {"mensaje": "Reglas actualizadas"}
