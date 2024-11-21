from Api.models.persona import Persona
from sqlalchemy.orm import Session
from Api.schemas.persona import PersonBase
from fastapi import HTTPException
import sys

def create_new_person(persona: PersonBase, db: Session):
    db_person = Persona(
        cedula=persona.cedula,
        nombre=persona.nombre,
        apellido=persona.apellido,
    )
    try:
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
        return db_person
    except Exception as e:
        db.rollback()
        print(f"Error al crear persona: {str(e)}", file=sys.stderr)
        raise HTTPException(status_code=500, detail="No se pudo agregar la persona")

def update_persona(persona: PersonBase, db: Session):
    db_persona = db.query(Persona).filter(Persona.cedula == persona.cedula).first()
    if db_persona is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    
    try:
        db_persona.nombre = persona.nombre
        db_persona.apellido = persona.apellido
        db.commit()
        db.refresh(db_persona)
        return db_persona
    except Exception as e:
        db.rollback()
        print(f"Error al actualizar persona: {str(e)}", file=sys.stderr)
        raise HTTPException(status_code=500, detail="No se pudo actualizar la persona")

    
def delete_persona(persona_id: int, db: Session):
    db_persona = db.query(Persona).filter(Persona.id_persona == persona_id).first()
    if db_persona is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    
    try:
        db.delete(db_persona)
        db.commit()
        return {"message": "Persona eliminada correctamente"} 
    except Exception as e:
        db.rollback()
        print(f"Error al eliminar persona: {str(e)}", file=sys.stderr)
        raise HTTPException(status_code=500, detail="No se pudo eliminar la persona")

