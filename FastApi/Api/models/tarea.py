from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from Api.models.base_class import Base
from Api.models.categoria import Categoria  # Asegúrate de importar el modelo Categoria

# Modelo SQLAlchemy para Tarea
class Tarea(Base):
    __tablename__ = "tareas"
    
    id_tarea = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    
    # id_categoria es ahora una clave foránea
    id_categoria = Column(Integer, ForeignKey("categoria.id_categoria"), nullable=False)  # Definimos la clave foránea aquí
    
    # Relación con el modelo Categoria
    categoria = relationship("Categoria", back_populates="tareas")  # Relación con Categoria
    
    tareas_programadas = relationship("TareaProgramada", back_populates="tarea")  # Relación con TareaProgramada
