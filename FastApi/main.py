from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Api.routes import persona, tarea, tarea_programada
from core.config import settings

api_router = APIRouter()

api_router.include_router(persona.router, prefix="/persona", tags=["Persona"])
api_router.include_router(tarea.router, prefix="/tarea", tags=["Tarea"])
api_router.include_router(tarea_programada.router, prefix="/tareaProgramada", tags=["Tarea Programada"])


app = FastAPI(
    title=settings.PROJECT_NAME, 
    version=settings.PROJECT_VERSION, 
    description=settings.PROJECT_DESCRIPTION
)

# Configurar CORS con especificidad
origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["Authorization", "Content-Type"],  # Encabezados permitidos
)

app.include_router(api_router)