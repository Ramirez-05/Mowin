from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Api.schemas.tarea_programada import PersonaConTareasRead
from db.connection import get_session
from core.utils import serverStatus
from Api.models.persona import Persona
from datetime import date
from Api.crud.tarea import actualizar_categoria_tareas
from Api.models.categoria import Categoria

router = APIRouter()

@router.get("/get-tareas-programadas", response_model=list[PersonaConTareasRead])
async def get_tareas_programadas(db: Session = Depends(get_session)):
    if not serverStatus(db):
        raise HTTPException(status_code=503, detail="La base de datos no está disponible")
    
    personas = db.query(Persona).all()

    result = []
    for persona in personas:
        # Check if the person has any assigned tasks
        if persona.tareas_programadas:
            tareas_programadas = []
            for tarea_programada in persona.tareas_programadas:
                tarea = tarea_programada.tarea
                categoria = tarea.categoria
                tareas_actualizadas = actualizar_categoria_tareas([tarea], es_get=True)
                tarea_actualizada = tareas_actualizadas[0]
                categoria = db.query(Categoria).filter(Categoria.id_categoria == tarea_actualizada.id_categoria).first()
                fecha_vencimiento = tarea_actualizada.fecha_vencimiento.strftime('%Y-%m-%d') if isinstance(tarea_actualizada.fecha_vencimiento, date) else tarea_actualizada.fecha_vencimiento
                
                tareas_programadas.append({
                    "id_tarea": tarea_actualizada.id_tarea,
                    "titulo": tarea_actualizada.titulo,
                    "descripcion": tarea_actualizada.descripcion,
                    "fecha_vencimiento": fecha_vencimiento,
                    "categoria": {
                        "id_categoria": categoria.id_categoria,
                        "nombre": categoria.nombre
                    }
                })
            
            result.append({
                "cedula": persona.cedula,
                "nombre": persona.nombre,
                "apellido": persona.apellido,
                "id_persona": persona.id_persona,
                "tareas_programadas": tareas_programadas
            })
    
    return result

