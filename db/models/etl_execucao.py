from sqlalchemy import Column, DateTime, Float, Integer, String

from db.base import Base


class ETLExecucao(Base):
    __tablename__ = "etl_execucao"

    id = Column(Integer, primary_key=True)
    ano = Column(Integer, nullable=False, index=True)
    inicio = Column(DateTime, nullable=False)
    fim = Column(DateTime)
    tempo_leitura = Column(Float, default=0)
    tempo_processamento = Column(Float, default=0)
    tempo_sqlite = Column(Float, default=0)
    tempo_parquet = Column(Float, default=0)
    memoria = Column(Float)
    status = Column(String, nullable=False, default="iniciado")
    parquet_path = Column(String)
    erro = Column(String)
