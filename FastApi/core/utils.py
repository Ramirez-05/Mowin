from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from Api.models.persona import Persona
from sqlalchemy.orm import Session
from sqlalchemy import select
from Api.models.categoria import Categoria
from fastapi import HTTPException

# Función para verificar si el servidor de base de datos está disponible y acepta conexiones
def serverStatus(db):
    try:
        db.execute(text('SELECT 1'))
        return True
    except OperationalError:
        return False

# funcion para verificar si la cedula ya existe en la base de datos
def is_cedula_duplicated(cedula: str, db: Session) -> bool:
    return db.query(Persona).filter(Persona.cedula == cedula).first() is not None

# funcion para verificar si la categoria ya existe en la base de datos
def check_categoria_existente(id_categoria: int, db: Session):
    categoria = db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="La categoría no existe")
    return categoria