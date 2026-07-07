from pathlib import Path

import polars as pl

from core.config import data_dir_for_year, resolve_data_dir_for_year
from etl.base import BaseETL
from etl.layouts.common import garantir_colunas_indicadores, selecionar_colunas_padrao
from etl.mappings import INDICADORES, MAPPING_2003


class ETL2003(BaseETL):
    ano = 2003
    descricao_layout = "layout_2003"

    def transformar(self) -> pl.DataFrame:
        pasta = self._diretorio_dados()
        frames: list[pl.DataFrame] = []
        for nome_arquivo, mapping in MAPPING_2003.items():
            caminho = pasta / nome_arquivo
            if not caminho.exists():
                continue
            df = self._processar_arquivo(caminho, mapping)
            if df.height:
                frames.append(df.with_columns(pl.lit(nome_arquivo).alias("ARQUIVO_ORIGEM")))

        if not frames:
            raise FileNotFoundError("Nenhum arquivo de 2003 foi encontrado/processado")
        return pl.concat(frames, how="diagonal_relaxed")

    def _diretorio_dados(self) -> Path:
        base = resolve_data_dir_for_year(self.origem, self.ano) if self.origem else data_dir_for_year(self.ano)
        if base.is_dir() and any((base / nome_arquivo).exists() for nome_arquivo in MAPPING_2003):
            return base
        if base.is_dir() and base.name.upper() == "DADOS":
            return base
        candidatos = [path for path in base.rglob("*") if path.is_dir() and path.name.upper() == "DADOS"]
        if not candidatos:
            raise FileNotFoundError(f"Diretorio DADOS nao encontrado em {base}")
        return candidatos[0]

    def _processar_arquivo(self, caminho: Path, mapping: dict[str, list[str]]) -> pl.DataFrame:
        df = pl.read_csv(
            caminho,
            separator=self.detectar_separador(caminho),
            encoding="latin1",
            infer_schema_length=10000,
            ignore_errors=True,
        )
        df = df.rename({col: col.strip().upper() for col in df.columns})
        if {"SIGLA_UF_CURSO", "CATEGADM", "NOMEORGACAD"}.issubset(df.columns):
            df = df.filter(
                (pl.col("SIGLA_UF_CURSO") == "PR")
                & (pl.col("CATEGADM").cast(pl.Utf8).str.contains("(?i)Estadual"))
                & (pl.col("NOMEORGACAD") == "Universidade")
            )
        if df.height == 0:
            return df

        df = garantir_colunas_indicadores(df)
        for indicador, colunas_origem in mapping.items():
            existentes = [col for col in colunas_origem if col in df.columns]
            if existentes:
                df = df.with_columns(
                    pl.sum_horizontal(
                        [pl.col(col).cast(pl.Int64, strict=False).fill_null(0) for col in existentes]
                    ).alias(indicador)
                )

        for indicador in INDICADORES:
            if indicador not in df.columns:
                df = df.with_columns(pl.lit(0, dtype=pl.Int64).alias(indicador))
        return selecionar_colunas_padrao(df)
