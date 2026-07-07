from pathlib import Path

import polars as pl

from etl.mappings import INDICADORES


COLUNAS_BASE = [
    "CO_IES",
    "SG_IES",
    "NO_IES",
    "CO_CURSO",
    "NO_CURSO",
    "SG_UF",
    "SIGLA_UF_CURSO",
    "NO_MUNICIPIO",
    "NO_ORGANIZACAO_ACADEMICA",
    "NO_CATEGORIA_ADMINISTRATIVA",
    "NOMEORGACAD",
    "CATEGADM",
    "TP_NIVEL_ACADEMICO",
    "TP_GRAU_ACADEMICO",
    "TP_MODALIDADE_ENSINO",
    "NO_CINE_ROTULO",
    "NO_CINE_AREA_GERAL",
]


def encontrar_diretorio_dados(base: Path, nome_preferido: str = "dados") -> Path:
    if base.is_dir() and base.name.lower() == nome_preferido.lower():
        return base
    candidatos = [path for path in base.rglob("*") if path.is_dir() and path.name.lower() == nome_preferido.lower()]
    if not candidatos:
        raise FileNotFoundError(f"Diretorio '{nome_preferido}' nao encontrado em {base}")
    return candidatos[0]


def garantir_colunas_indicadores(df: pl.DataFrame) -> pl.DataFrame:
    missing = [col for col in INDICADORES if col not in df.columns]
    if not missing:
        return df
    return df.with_columns([pl.lit(0, dtype=pl.Int64).alias(col) for col in missing])


def selecionar_colunas_padrao(df: pl.DataFrame) -> pl.DataFrame:
    manter = [col for col in COLUNAS_BASE + INDICADORES if col in df.columns]
    return df.select(manter)
