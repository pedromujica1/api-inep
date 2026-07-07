from db.session import SessionLocal, init_db
from etl.runner import executar_etl

init_db()

with SessionLocal() as db:
    executar_etl(db, ano=2003)
    executar_etl(db, ano=2009)
    executar_etl(db, ano=2010)
    executar_etl(db, ano=2011)
    executar_etl(db, ano=2012)
    