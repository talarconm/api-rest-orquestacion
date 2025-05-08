from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="API Orquestación de Servicios Logísticos",
    version="1.0.0",
    debug=True
)

app.include_router(router)
