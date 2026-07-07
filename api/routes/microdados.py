from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.consulta import ConsultaRequest
from schemas.resposta import ConsultaResponse
from services.consulta_service import ConsultaService


router = APIRouter(prefix="/api/microdados", tags=["microdados"])


@router.post("/consultar", response_model=ConsultaResponse)
def consultar(request: ConsultaRequest, db: Session = Depends(get_db)) -> ConsultaResponse:
    return ConsultaService(db).consultar(request)
