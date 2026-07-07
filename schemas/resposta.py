from typing import Any

from pydantic import BaseModel


class ConsultaResponse(BaseModel):
    anos: list[int]
    indicadores: list[str]
    dimensao: str
    filtros: dict[str, list[Any]]
    total_registros: int
    dados: list[dict[str, Any]]
