from datetime import datetime
from pathlib import Path

from sqlalchemy.orm import Session

from etl.benchmark import registrar_execucao
from etl.factory import ETLFactory


def executar_etl(db: Session,ano: int,origem: str | None = None,recarregar_checkpoint: bool = False) -> Path:
    inicio = datetime.now()
    try:
        etl = ETLFactory.criar(ano, Path(origem) if origem else None)
        parquet = etl.executar(db, recarregar_checkpoint=recarregar_checkpoint)
        registrar_execucao(db, ano, inicio, "sucesso", str(parquet))
        return parquet
    except Exception as exc:
        db.rollback()
        registrar_execucao(db, ano, inicio, "erro", erro=str(exc))
        raise
