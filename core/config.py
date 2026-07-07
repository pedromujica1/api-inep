import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_RAW_DATA_DIR = BASE_DIR / "2-dados_brutos"
LEGACY_RAW_DATA_DIR = BASE_DIR / "etl" / "dados_brutos"
RAW_DATA_DIR = Path(
    os.getenv(
        "INEP_RAW_DATA_DIR",
        DEFAULT_RAW_DATA_DIR if DEFAULT_RAW_DATA_DIR.exists() else LEGACY_RAW_DATA_DIR,
    )
)
DATA_DIR = Path(os.getenv("INEP_DATA_DIR", RAW_DATA_DIR))
CHECKPOINT_DIR = Path(os.getenv("INEP_CHECKPOINT_DIR", BASE_DIR / "checkpoints"))
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'inep.sqlite3'}")


def resolve_data_dir_for_year(base: Path, ano: int) -> Path:
    if base.name == f"microdados-{ano}":
        return base

    candidato = base / f"microdados-{ano}"
    if candidato.exists():
        return candidato

    return base


def data_dir_for_year(ano: int) -> Path:
    env_dir = os.getenv(f"INEP_DATA_DIR_{ano}")
    if env_dir:
        return Path(env_dir)

    return resolve_data_dir_for_year(DATA_DIR, ano)
