from Api.models.tarea import Tarea
from sqlalchemy.orm import Session
from Api.schemas.tarea import TareaBase, TareaUpdate
from fastapi import HTTPException
import sys
from core.utils import check_categoria_existente
from datetime import datetime, timedelta

# Función para crear una tarea
def create_new_tarea(tarea: TareaBase, db: Session):
    tarea.id_categoria = tarea.id_categoria or 2
    check_categoria_existente(tarea.id_categoria, db)
    db_tarea = Tarea(
        titulo=tarea.titulo,
        descripcion=tarea.descripcion,
        fecha_vencimiento=tarea.fecha_vencimiento,
        id_categoria=tarea.id_categoria
    )
    try:
        db.add(db_tarea)
        db.commit()
        db.refresh(db_tarea)
        return db_tarea
    except Exception as e:
        db.rollback()
        print(f"Error al crear tarea: {str(e)}", file=sys.stderr)
        raise HTTPException(status_code=500, detail="No se pudo agregar la tarea")
    
# Función para actualizar una tarea
def update_tarea(tarea: TareaUpdate, db: Session):

    # Verifica si la categoría existe antes de actualizar la tarea
    check_categoria_existente(tarea.id_categoria, db)
    
    db_tarea = db.query(Tarea).filter(Tarea.id_tarea == tarea.id_tarea).first()
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="La tarea no existe")
    try:
        db_tarea.titulo = tarea.titulo
        db_tarea.descripcion = tarea.descripcion
        db_tarea.fecha_vencimiento = tarea.fecha_vencimiento
        db_tarea.id_categoria = tarea.id_categoria
        db.commit()
        db.refresh(db_tarea)
        return db_tarea
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="No se pudo actualizar la tarea")
    
# Función para eliminar una tarea
def delete_tarea(tarea_id: int, db: Session):
    db_tarea = db.query(Tarea).filter(Tarea.id_tarea == tarea_id).first()
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="La tarea no existe")
    try:
        db.delete(db_tarea)
        db.commit()
        return {"message": "Tarea eliminada correctamente"} 
    except Exception as e:
        db.rollback()
        print(f"Error al eliminar tarea: {str(e)}", file=sys.stderr)
        raise HTTPException(status_code=500, detail="No se pudo eliminar la tarea")


from datetime import datetime

def actualizar_categoria_tareas(tareas: list[Tarea], es_get: bool = False):
    for tarea in tareas:
        # Si estamos en un GET y la categoría es 4, no se modifica
        if es_get and tarea.id_categoria == 4:
            continue
        diferencia_dias = (datetime.today().date() - tarea.fecha_vencimiento).days 
        if diferencia_dias > 0: 
            tarea.id_categoria = 3  
    return tareas
