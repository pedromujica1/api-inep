from sqlalchemy import Column, Integer

from db.base import Base


class DimAno(Base):
    __tablename__ = "dim_ano"

    ano = Column(Integer, primary_key=True)
