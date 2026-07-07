from sqlalchemy import Column, Integer, String

from db.base import Base


class DimLayout(Base):
    __tablename__ = "dim_layout"

    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)
    ano_inicio = Column(Integer, nullable=False)
    ano_fim = Column(Integer, nullable=False)
