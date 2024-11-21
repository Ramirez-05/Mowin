from pydantic import BaseModel
from typing import List

# Esquema para Categoria
class CategoriaBase(BaseModel):
    id_categoria: int
    nombre: str

    class Config:
        orm_mode = True

# Esquema para Tarea (con categoría incluida)
class TareaBase(BaseModel):
    id_tarea: int
    titulo: str
    descripcion: str
    fecha_vencimiento: str
    categoria: CategoriaBase 

    class Config:
        orm_mode = True  

# Esquema para Persona con las tareas programadas
class PersonaConTareasRead(BaseModel):
    cedula: str
    nombre: str
    apellido: str
    id_persona: int
    tareas_programadas: List[TareaBase]

    class Config:
        orm_mode = True
