from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from Api.models.base_class import Base

# Modelo SQLAlchemy para Categoria
class Categoria(Base):
    __tablename__ = "categoria"
    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=True)
    tareas = relationship("Tarea", back_populates="categoria")  # Relación con Tarea

