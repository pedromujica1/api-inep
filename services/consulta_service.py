from sqlalchemy.orm import Session

from db.repositories.microdados_repository import MicrodadosRepository
from schemas.consulta import ConsultaRequest
from schemas.resposta import ConsultaResponse


class ConsultaService:
    def __init__(self, db: Session):
        self.repository = MicrodadosRepository(db)

    def consultar(self, request: ConsultaRequest) -> ConsultaResponse:
        dados = self.repository.consultar(
            anos=request.anos,
            indicadores=request.indicadores,
            dimensao=request.dimensao,
            filtros=request.filtros,
        )
        return ConsultaResponse(
            anos=request.anos,
            indicadores=list(request.indicadores),
            dimensao=request.dimensao,
            filtros=request.filtros,
            total_registros=len(dados),
            dados=dados,
        )
