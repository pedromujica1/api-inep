from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from core.config import DATABASE_URL


engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},future=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    from db import models  # noqa: F401
    from db.base import Base

    Base.metadata.create_all(bind=engine)
