from abc import ABC, abstractmethod
from pathlib import Path
from time import perf_counter

import polars as pl
from sqlalchemy.orm import Session

from etl.checkpoint import checkpoint_path
from etl.loader import SQLiteLoader


class BaseETL(ABC):
    ano: int
    descricao_layout: str

    def __init__(self, origem: Path | None = None):
        self.origem = origem

    def executar(self, db: Session, recarregar_checkpoint: bool = False) -> Path:
        destino = checkpoint_path(self.ano)
        if recarregar_checkpoint and destino.exists():
            df = pl.read_parquet(destino)
        else:
            df = self.transformar()
            destino.parent.mkdir(parents=True, exist_ok=True)
            df.write_parquet(destino, compression="zstd")

        SQLiteLoader(db).carregar(self.ano, df, str(destino))
        return destino

    @abstractmethod
    def transformar(self) -> pl.DataFrame:
        raise NotImplementedError

    @staticmethod
    def detectar_separador(caminho: Path) -> str:
        with caminho.open("r", encoding="latin1") as arquivo:
            linha = arquivo.readline()
        if "|" in linha:
            return "|"
        if "," in linha and ";" not in linha:
            return ","
        return ";"

    @staticmethod
    def cronometro() -> float:
        return perf_counter()
