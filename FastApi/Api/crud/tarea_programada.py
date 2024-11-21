from Api.models.tarea_programada import TareaProgramada
from sqlalchemy.orm import Session
from Api.schemas.tarea_programada import TareaProgramadaBase
from fastapi import HTTPException
import sys

# Función para crear una nueva tarea programada
def create_new_tarea_programada(tarea_programada: TareaProgramadaBase, db: Session):
    db_tarea_programada = TareaProgramada(
        id_persona=tarea_programada.id_persona,
        id_tarea=tarea_programada.id_tarea,
    )
    try:
        db.add(db_tarea_programada)
        db.commit()
        db.refresh(db_tarea_programada)
        return db_tarea_programada
    except Exception as e:
        db.rollback()
        print(f"Error al crear tarea programada: {str(e)}", file=sys.stderr)
        raise HTTPException(status_code=500, detail="No se pudo agregar la tarea programada")

# Función para actualizar una tarea programada
def update_tarea_programada(tarea_programada: TareaProgramadaBase, db: Session):
    db_tarea_programada = db.query(TareaProgramada).filter(TareaProgramada.id_tarea_p == tarea_programada.id_tarea_p).first()
    if db_tarea_programada is None:
        raise HTTPException(status_code=404, detail="La tarea programada no existe")
    
    try:
        db_tarea_programada.id_persona = tarea_programada.id_persona
        db_tarea_programada.id_tarea = tarea_programada.id_tarea
        db.commit()
        db.refresh(db_tarea_programada)
        return db_tarea_programada
    except Exception as e:
        db.rollback()
        print(f"Error al actualizar tarea programada: {str(e)}", file=sys.stderr)
        raise HTTPException(status_code=500, detail="No se pudo actualizar la tarea programada")
    

# Función para eliminar una tarea programada
def delete_tarea_programada(tarea_programada_id: int, db: Session):
    db_tarea_programada = db.query(TareaProgramada).filter(TareaProgramada.id_tarea_p == tarea_programada_id).first()
    if db_tarea_programada is None:
        raise HTTPException(status_code=404, detail="La tarea programada no existe")
    
    try:
        db.delete(db_tarea_programada)
        db.commit()
        return {"message": "Tarea programada eliminada correctamente"} 
    except Exception as e:
        db.rollback()
        print(f"Error al eliminar tarea programada: {str(e)}", file=sys.stderr)
        raise HTTPException(status_code=500, detail="No se pudo eliminar la tarea programada")
