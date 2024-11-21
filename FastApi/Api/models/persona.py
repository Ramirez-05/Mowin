# persona.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Api.models.base_class import Base
from Api.models.tarea_programada import TareaProgramada

class Persona(Base):
    __tablename__ = "persona"
    id_persona = Column(Integer, primary_key=True, index=True)
    cedula = Column(String(20), nullable=False, unique=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    
    
    tareas_programadas = relationship("TareaProgramada", back_populates="persona") # Relación uno a muchos con la tabla TareaProgramada
