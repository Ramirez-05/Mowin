from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Api.schemas.persona import PersonBase, PersonaRead
from db.connection import get_session
from core.utils import serverStatus, is_cedula_duplicated
from Api.crud.persona import create_new_person, update_persona, delete_persona
from Api.models.persona import Persona

router = APIRouter()

# Ruta para crear una persona
@router.post("/create-persona", response_model=PersonaRead)
async def add_person(persona: PersonBase, db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="La base de datos no esta disponible")
    if is_cedula_duplicated(persona.cedula, db):
        raise HTTPException(status_code=400, detail="La cédula ya está registrada")
    return create_new_person(persona, db)

# Ruta para obtener una persona por su id
@router.get("/get-persona", response_model=PersonaRead)
async def get_persona(persona_id: int, db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="La base de datos no esta disponible")
    persona = db.query(Persona).filter(Persona.id_persona == persona_id).first()
    if persona is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    return persona

# Ruta para obtener todas las personas
@router.get("/get-all-personas")
async def get_all_personas(db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="La base de datos no esta disponible")
    personas = db.query(Persona).all()
    return personas

# Ruta para actualizar una persona
@router.put("/update-persona", response_model=PersonaRead) 
def update_persona_router(persona: PersonBase, db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="La base de datos no esta disponible")
    return update_persona(persona, db)

# Ruta para eliminar una persona
@router.delete("/delete-persona")
async def delete_persona_router(persona_id: int, db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="La base de datos no esta disponible")
    return delete_persona(persona_id, db)  
