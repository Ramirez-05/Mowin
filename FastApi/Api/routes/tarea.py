from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Api.schemas.tarea import TareaBase, TareaRead
from db.connection import get_session
from core.utils import serverStatus
from Api.crud.tarea import create_new_tarea, update_tarea, delete_tarea, actualizar_categoria_tareas
from Api.models.tarea import Tarea
from Api.models.categoria import Categoria

router = APIRouter()

# Ruta para crear una tarea
@router.post("/create_tarea", response_model=TareaRead)
def create_tarea_route(tarea: TareaBase, db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="El servidor no está disponible.")
    return create_new_tarea(tarea, db)

@router.get("/get_tareas", response_model=list[TareaRead])
def get_tareas(db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="El servidor no está disponible.")
    tareas = db.query(Tarea).all()
    tareas_actualizadas = actualizar_categoria_tareas(tareas, es_get=True)
    tareas_con_categoria = []
    for tarea in tareas_actualizadas:
        categoria = db.query(Categoria).filter(Categoria.id_categoria == tarea.id_categoria).first()
        if categoria:
            tarea_data = TareaRead(
                id_tarea=tarea.id_tarea,
                titulo=tarea.titulo,
                descripcion=tarea.descripcion,
                fecha_vencimiento=tarea.fecha_vencimiento,
                categoria_nombre=categoria.nombre
            )
            tareas_con_categoria.append(tarea_data)
    return tareas_con_categoria

# Ruta para obtener una tarea por su id
@router.get("/get_tarea", response_model=TareaRead)
def get_tarea(id_tarea: int, db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="El servidor no está disponible.")
    tarea = db.query(Tarea).filter(Tarea.id_tarea == id_tarea).first()
    if tarea is None:
        raise HTTPException(status_code=404, detail="La tarea no existe.")
    tareas_actualizadas = actualizar_categoria_tareas([tarea], es_get=True)
    tarea_actualizada = tareas_actualizadas[0]
    categoria = db.query(Categoria).filter(Categoria.id_categoria == tarea_actualizada.id_categoria).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="La categoría asociada no existe.")
    tarea_con_categoria = TareaRead(
        id_tarea=tarea_actualizada.id_tarea,
        titulo=tarea_actualizada.titulo,
        descripcion=tarea_actualizada.descripcion,
        fecha_vencimiento=tarea_actualizada.fecha_vencimiento,
        categoria_nombre=categoria.nombre
    )
    return tarea_con_categoria

# Ruta para actualizar una tarea
@router.put("/update_tarea", response_model=TareaRead)
def update_tarea_route(tarea: TareaRead, db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="El servidor no está disponible.")
    return update_tarea(tarea, db)

# Ruta para eliminar una tarea
@router.delete("/delete_tarea")
def delete_tarea_rouet(id_tarea: int, db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="El servidor no está disponible.")
    return delete_tarea(id_tarea,db)