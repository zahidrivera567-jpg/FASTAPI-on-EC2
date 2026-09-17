from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    correo: str
    facturas: List["Factura"] = Relationship(back_populates="cliente")

class Factura(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    monto: float
    descripcion: str
    cliente_id: Optional[int] = Field(default=None, foreign_key="cliente.id")
    cliente: Optional[Cliente] = Relationship(back_populates="facturas")