from Api.models.tarea_programada import TareaProgramada
from sqlalchemy.orm import Session
from Api.schemas.tarea_programada import TareaProgramadaNew
from fastapi import HTTPException
import sys
from Api.models.tarea import Tarea
from Api.models.persona import Persona


# Función para crear una nueva tarea programada
from sqlalchemy.orm import Session
from Api.models.tarea_programada import TareaProgramada
from Api.schemas.tarea_programada import TareaProgramadaNew
from fastapi import HTTPException
import sys
from Api.models.tarea import Tarea
from Api.models.persona import Persona


# Función para crear una nueva tarea programada
def create_new_tarea_programada(tarea_programada: TareaProgramadaNew, db: Session):
    # verificar si la tarea existe
    tarea = db.query(Tarea).filter(Tarea.id_tarea == tarea_programada.id_tarea).first()
    if tarea is None:
        raise HTTPException(status_code=404, detail="La tarea no existe")
    
    # verificar si la persona existe
    persona = db.query(Persona).filter(Persona.id_persona == tarea_programada.id_persona).first()
    if persona is None:
        raise HTTPException(status_code=404, detail="La persona no existe")

    # Actualizar la categoría de la tarea a 4
    tarea.id_categoria = 1

    db_tarea_programada = TareaProgramada(
        id_persona=tarea_programada.id_persona,
        id_tarea=tarea_programada.id_tarea,
    )
    try:
        # Guardar los cambios en la tarea y la nueva tarea programada
        db.add(db_tarea_programada)
        db.commit()
        db.refresh(db_tarea_programada)
        return db_tarea_programada
    except Exception as e:
        db.rollback()
        print(f"Error al crear tarea programada: {str(e)}", file=sys.stderr)
        raise HTTPException(status_code=500, detail="No se pudo agregar la tarea programada")
