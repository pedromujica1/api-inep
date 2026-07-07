from sqlalchemy import Column, Integer, JSON

from db.base import Base


class CamposDisponiveis(Base):
    __tablename__ = "campos_disponiveis"

    ano = Column(Integer, primary_key=True)
    indicadores = Column(JSON, nullable=False, default=list)
    dimensoes = Column(JSON, nullable=False, default=list)
