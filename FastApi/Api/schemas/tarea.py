from pydantic import BaseModel, field_validator
from datetime import date

class TareaBase(BaseModel):
    titulo: str
    descripcion: str
    fecha_vencimiento: date
    id_categoria: int

    # Validación combinada para titulo y descripcion
    @field_validator('titulo', 'descripcion')
    def check_not_empty(cls, v, field):
        if not v or v.strip() == "":
            raise ValueError(f"{field.name} no puede estar vacío.")
        return v

    # Validación para la fecha de vencimiento (no puede ser una fecha pasada)
    @field_validator('fecha_vencimiento')
    def check_fecha_vencimiento(cls, v):
        if v < date.today():
            raise ValueError("La fecha de vencimiento no puede ser una fecha pasada.")
        return v

    # Validación para el id_categoria
    @field_validator('id_categoria')
    def check_categoria_valida(cls, v):
        if v <= 0:
            raise ValueError("El ID de categoría debe ser un valor positivo.")
        return v

    class Config:
        str_strip_whitespace = True


class TareaRead(BaseModel):
    id_tarea: int
    titulo: str
    descripcion: str
    fecha_vencimiento: date
    categoria_nombre: str 

    class Config:
        str_strip_whitespace = True
