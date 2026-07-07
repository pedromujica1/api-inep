from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from db.models import CamposDisponiveis, DimCurso, DimIES, FatoIndicadores


INDICADOR_COLS = {
    "QT_VAGA": FatoIndicadores.qt_vaga,
    "QT_ING": FatoIndicadores.qt_ing,
    "QT_MAT": FatoIndicadores.qt_mat,
    "QT_CONC": FatoIndicadores.qt_conc,
    "QT_SIT_TRANCADA": FatoIndicadores.qt_sit_trancada,
    "QT_SIT_DESVINCULADO": FatoIndicadores.qt_sit_desvinculado,
    "QT_SIT_TRANSFERIDO": FatoIndicadores.qt_sit_transferido,
    "QT_PERDA": FatoIndicadores.qt_perda,
}

DIMENSAO_COLS = {
    "ano": (FatoIndicadores.ano, "ano"),
    "instituicao": (DimIES.nome, "instituicao"),
    "curso": (DimCurso.nome, "curso"),
    "area": (DimCurso.area, "area"),
    "area_geral": (DimCurso.area_geral, "area_geral"),
    "modalidade": (DimCurso.modalidade, "modalidade"),
}

FILTRO_COLS = {
    "ano": FatoIndicadores.ano,
    "co_ies": FatoIndicadores.co_ies,
    "instituicao": DimIES.nome,
    "regiao": DimIES.regiao,
    "uf": DimIES.uf,
    "municipio": DimIES.municipio,
    "co_curso": DimCurso.co_curso,
    "curso": DimCurso.nome,
    "area": DimCurso.area,
    "area_geral": DimCurso.area_geral,
    "modalidade": DimCurso.modalidade,
}


class MicrodadosRepository:
    def __init__(self, db: Session):
        self.db = db

    def consultar(self,anos: list[int],indicadores: list[str],dimensao: str,filtros: dict[str, list[Any]]) -> list[dict[str, Any]]:
        dim_col, dim_label = DIMENSAO_COLS[dimensao]
        
        metricas = [
            func.coalesce(func.sum(INDICADOR_COLS[indicador]), 0).label(indicador)
            for indicador in indicadores
        ]
        stmt = (
            select(FatoIndicadores.ano, dim_col.label(dim_label), *metricas)
            .join(DimIES, FatoIndicadores.co_ies == DimIES.co_ies)
            .join(DimCurso, FatoIndicadores.curso_id == DimCurso.id)
            .where(FatoIndicadores.ano.in_(anos))
            .group_by(FatoIndicadores.ano, dim_col)
            .order_by(FatoIndicadores.ano, dim_col)
        )

        for nome, valores in filtros.items():
            if not valores or nome not in FILTRO_COLS:
                continue
            stmt = stmt.where(FILTRO_COLS[nome].in_(valores))

        return [dict(row._mapping) for row in self.db.execute(stmt).all()]

    def buscar_campos_disponiveis(self, ano: int) -> CamposDisponiveis | None:
        return self.db.get(CamposDisponiveis, ano)
