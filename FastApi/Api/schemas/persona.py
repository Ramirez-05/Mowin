
from pydantic import BaseModel, field_validator

class PersonBase(BaseModel):
    cedula: str
    nombre: str
    apellido: str

    # Valida que los campos cedula, nombres y apellidos no estén vacíos
    @field_validator('cedula', 'nombre', 'apellido')
    def check_not_empty(cls, v):
        if not v or v.strip() == "":
            raise ValueError(f"{cls.__name__} no puede estar vacío")
        return v

    class Config:
        str_strip_whitespace = True 


class PersonaRead(PersonBase):
    id_persona: int

