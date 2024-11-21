# tarea_programada.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Api.models.base_class import Base

# Si la clase Tarea está en otro archivo, la importamos
from Api.models.tarea import Tarea

# Modelo SQLAlchemy para TareaProgramada
class TareaProgramada(Base):
    __tablename__ = "tarea_programada"
    id_tarea_p = Column(Integer, primary_key=True, index=True)
    id_persona = Column(Integer, ForeignKey("persona.id_persona"), nullable=True)
    id_tarea = Column(Integer, ForeignKey("tareas.id_tarea"), nullable=False)
    
    # Relación con Persona
    persona = relationship("Persona", back_populates="tareas_programadas")  
    
    # Relación con Tarea
    tarea = relationship("Tarea", back_populates="tareas_programadas")  
