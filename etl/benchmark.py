from datetime import datetime

from sqlalchemy.orm import Session

from db.models import ETLExecucao


def registrar_execucao(db: Session,ano: int,inicio: datetime,status: str,parquet_path: str | None = None,erro: str | None = None) -> None:
    
    db.add(ETLExecucao(ano=ano,inicio=inicio,fim=datetime.now(),status=status,parquet_path=parquet_path,erro=erro))
    db.commit()
