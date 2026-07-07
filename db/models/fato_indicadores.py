from sqlalchemy import Column, ForeignKey, Index, Integer
from sqlalchemy.orm import relationship

from db.base import Base


class FatoIndicadores(Base):
    __tablename__ = "fato_indicadores"
    __table_args__ = ( Index("idx_fato_ano_ies", "ano", "co_ies"), Index("idx_fato_ano_curso", "ano", "curso_id"), Index("idx_fato_ies_curso_ano", "co_ies", "curso_id", "ano"))

    id = Column(Integer, primary_key=True)
    ano = Column(Integer, ForeignKey("dim_ano.ano"), nullable=False, index=True)
    co_ies = Column(Integer, ForeignKey("dim_ies.co_ies"), nullable=False, index=True)
    curso_id = Column(Integer, ForeignKey("dim_curso.id"), nullable=False, index=True)
    qt_vaga = Column(Integer, default=0)
    qt_ing = Column(Integer, default=0)
    qt_mat = Column(Integer, default=0)
    qt_conc = Column(Integer, default=0)
    qt_sit_trancada = Column(Integer, default=0)
    qt_sit_desvinculado = Column(Integer, default=0)
    qt_sit_transferido = Column(Integer, default=0)
    qt_perda = Column(Integer, default=0)

    ies = relationship("DimIES", back_populates="indicadores")
    curso = relationship("DimCurso", back_populates="indicadores")
