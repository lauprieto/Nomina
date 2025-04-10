from sqlalchemy import Column, Integer, Float, String
from .database import Base

class Nomina(Base):
    __tablename__ = "nominas"

    id = Column(Integer, primary_key=True, index=True)
    tipo_contrato = Column(String)
    salario_bruto = Column(Float)
    descuentos = Column(Float)
    salario_neto = Column(Float)
    salud = Column(Float)
    pension = Column(Float)
    cesantias = Column(Float)
