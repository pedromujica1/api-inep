from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from db.base import Base


class DimCurso(Base):
    __tablename__ = "dim_curso"
    __table_args__ = (
        UniqueConstraint("co_curso", "co_ies", name="uq_dim_curso_co_curso_co_ies"),
    )

    id = Column(Integer, primary_key=True)
    co_curso = Column(Integer, nullable=False, index=True)
    co_ies = Column(Integer, ForeignKey("dim_ies.co_ies"), nullable=False, index=True)
    nome = Column(String)
    area = Column(String)
    area_geral = Column(String)
    nivel = Column(String)
    grau = Column(String)
    modalidade = Column(String, index=True)

    ies = relationship("DimIES", back_populates="cursos")
    indicadores = relationship("FatoIndicadores", back_populates="curso")
