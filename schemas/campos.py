from pydantic import BaseModel


class CamposDisponiveisResponse(BaseModel):
    ano: int
    indicadores: list[str]
    dimensoes: list[str]
