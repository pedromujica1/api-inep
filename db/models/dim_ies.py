from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base import Base


class DimIES(Base):
    __tablename__ = "dim_ies"

    co_ies = Column(Integer, primary_key=True)
    sigla = Column(String)
    nome = Column(String)
    org_acad = Column(String)
    categoria_adm = Column(String)
    municipio = Column(String)
    uf = Column(String, index=True)
    regiao = Column(String, index=True)

    cursos = relationship("DimCurso", back_populates="ies")
    indicadores = relationship("FatoIndicadores", back_populates="ies")
