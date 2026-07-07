from pathlib import Path

from core.config import CHECKPOINT_DIR


def checkpoint_path(ano: int) -> Path:
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    return CHECKPOINT_DIR / f"microdados_{ano}.parquet"
