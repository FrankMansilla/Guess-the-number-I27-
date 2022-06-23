from email.mime import base
from sqlalchemy import Column, column #Campo de la Tabla
from sqlalchemy import ForeignKey # para mapear una clave externa a la tabla
from sqlalchemy import Integer, String, Float # Tipos de datos de la tabla

from sqlalchemy.orm import relationship # Genera una relacion entre tablas

from app.utils.db import Base 


class user(Base): 
    __tablename__ = "user_account" 
    id = column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(100))
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
