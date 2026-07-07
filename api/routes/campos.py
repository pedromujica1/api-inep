from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.repositories.microdados_repository import MicrodadosRepository
from db.session import get_db
from schemas.campos import CamposDisponiveisResponse


router = APIRouter(prefix="/api/campos", tags=["campos"])


@router.get("/{ano}", response_model=CamposDisponiveisResponse)
def campos_disponiveis(ano: int, db: Session = Depends(get_db)) -> CamposDisponiveisResponse:
    campos = MicrodadosRepository(db).buscar_campos_disponiveis(ano)
    if campos is None:
        raise HTTPException(status_code=404, detail="Campos nao encontrados para o ano")
    return CamposDisponiveisResponse(ano=campos.ano,indicadores=campos.indicadores,dimensoes=campos.dimensoes) # type: ignore
