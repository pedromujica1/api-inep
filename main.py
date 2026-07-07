from fastapi import FastAPI

from api.routes import campos, debug, microdados
from db.session import init_db


def create_app() -> FastAPI:
    init_db()
    app = FastAPI(title="API INEP - Universidades Estaduais do Parana")
    app.include_router(microdados.router)
    app.include_router(campos.router)
    app.include_router(debug.router)
    return app


app = create_app()
