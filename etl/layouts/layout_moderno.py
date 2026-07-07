from pathlib import Path

import polars as pl

from core.config import data_dir_for_year, resolve_data_dir_for_year
from etl.base import BaseETL
from etl.layouts.common import encontrar_diretorio_dados, garantir_colunas_indicadores, selecionar_colunas_padrao
from etl.mappings import INDICADORES


class ETLModerno(BaseETL):
    descricao_layout = "layout_moderno"

    def __init__(self, ano: int, origem: Path | None = None):
        if ano < 2009 or ano > 2024:
            raise ValueError("ETLModerno suporta anos de 2009 a 2024")
        self.ano = ano
        super().__init__(origem=origem)

    def transformar(self) -> pl.DataFrame:
        caminho = self._arquivo_microdados()
        df = pl.read_csv(
            caminho,
            separator=self.detectar_separador(caminho),
            encoding="latin1",
            infer_schema_length=10000,
            ignore_errors=True,
        )
        df = df.rename({col: col.strip().upper() for col in df.columns})
        df = self._filtrar_universidades_estaduais_pr(df)
        df = garantir_colunas_indicadores(df)
        return selecionar_colunas_padrao(df)

    def _arquivo_microdados(self) -> Path:
        base = resolve_data_dir_for_year(self.origem, self.ano) if self.origem else data_dir_for_year(self.ano)
        nomes = [
            f"MICRODADOS_CADASTRO_CURSOS_{self.ano}.CSV",
            f"MICRODADOS_CADASTRO_CURSOS_{self.ano}.csv",
        ]
        if base.is_dir():
            for nome in nomes:
                caminho = base / nome
                if caminho.exists():
                    return caminho

        pasta = encontrar_diretorio_dados(base)
        for nome in nomes:
            caminho = pasta / nome
            if caminho.exists():
                return caminho
        raise FileNotFoundError(f"Arquivo de cursos de {self.ano} nao encontrado em {pasta}")

    def _filtrar_universidades_estaduais_pr(self, df: pl.DataFrame) -> pl.DataFrame:
        if {"TP_ORGANIZACAO_ACADEMICA", "TP_CATEGORIA_ADMINISTRATIVA", "SG_UF"}.issubset(df.columns):
            return df.filter(
                (pl.col("TP_ORGANIZACAO_ACADEMICA").cast(pl.Int64, strict=False) == 1)
                & (pl.col("TP_CATEGORIA_ADMINISTRATIVA").cast(pl.Int64, strict=False) == 2)
                & (pl.col("SG_UF") == "PR")
            )
        return df
