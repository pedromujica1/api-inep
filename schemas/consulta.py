from typing import Any, Literal

from pydantic import BaseModel, Field, validator


Indicador = Literal[
    "QT_VAGA",
    "QT_ING",
    "QT_MAT",
    "QT_CONC",
    "QT_SIT_TRANCADA",
    "QT_SIT_DESVINCULADO",
    "QT_SIT_TRANSFERIDO",
    "QT_PERDA",
]

Dimensao = Literal["instituicao", "curso", "area", "area_geral", "modalidade", "ano"]


class ConsultaRequest(BaseModel):
    anos: list[int] = Field(..., min_items=1)
    indicadores: list[Indicador] = Field(..., min_items=1)
    dimensao: Dimensao
    filtros: dict[str, list[Any]] = Field(default_factory=dict)

    @validator("anos")
    def anos_suportados(cls, anos: list[int]) -> list[int]:
        invalidos = [ano for ano in anos if ano < 2003 or ano > 2024]
        if invalidos:
            raise ValueError("anos devem estar entre 2003 e 2024")
        return sorted(set(anos))
