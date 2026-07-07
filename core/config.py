import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = Path(os.getenv("INEP_RAW_DATA_DIR", BASE_DIR / "etl" / "dados_brutos"))
DATA_DIR = Path(os.getenv("INEP_DATA_DIR", RAW_DATA_DIR))
CHECKPOINT_DIR = Path(os.getenv("INEP_CHECKPOINT_DIR", BASE_DIR / "checkpoints"))
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'inep.sqlite3'}")


def data_dir_for_year(ano: int) -> Path:
    return Path(os.getenv(f"INEP_DATA_DIR_{ano}", DATA_DIR / f"microdados-{ano}"))
