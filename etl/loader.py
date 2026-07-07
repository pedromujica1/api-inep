import zlib
from typing import Any

import polars as pl
from sqlalchemy import delete, select
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

from db.models import CamposDisponiveis, DimAno, DimCurso, DimIES, FatoIndicadores
from etl.mappings import DIMENSOES, INDICADORES, REGIAO_POR_UF


class SQLiteLoader:
    def __init__(self, db: Session):
        self.db = db

    def carregar(self, ano: int, df: pl.DataFrame, parquet_path: str | None = None) -> None:
        self.db.execute(delete(FatoIndicadores).where(FatoIndicadores.ano == ano))
        self._upsert(DimAno, {"ano": ano}, ["ano"])
        self._upsert(
            CamposDisponiveis,
            {"ano": ano, "indicadores": INDICADORES, "dimensoes": DIMENSOES},
            ["ano"],
        )

        for row in df.to_dicts():
            co_ies = self._int_or_none(row.get("CO_IES"))
            if co_ies is None:
                continue
            uf = self._text(row.get("SG_UF") or row.get("SIGLA_UF_CURSO") or "PR")
            self._upsert(
                DimIES,
                {
                    "co_ies": co_ies,
                    "sigla": self._text(row.get("SG_IES")),
                    "nome": self._text(row.get("NO_IES")),
                    "org_acad": self._text(row.get("NO_ORGANIZACAO_ACADEMICA") or row.get("NOMEORGACAD")),
                    "categoria_adm": self._text(row.get("NO_CATEGORIA_ADMINISTRATIVA") or row.get("CATEGADM")),
                    "municipio": self._text(row.get("NO_MUNICIPIO") or row.get("MUNICIPIO")),
                    "uf": uf,
                    "regiao": REGIAO_POR_UF.get(uf, "sul"), # type: ignore
                },
                ["co_ies"],
            )

            co_curso = self._co_curso(row)
            self._upsert(
                DimCurso,
                {
                    "co_curso": co_curso,
                    "co_ies": co_ies,
                    "nome": self._text(row.get("NO_CURSO")),
                    "area": self._text(row.get("NO_CINE_ROTULO") or row.get("AREA")),
                    "area_geral": self._text(row.get("NO_CINE_AREA_GERAL") or row.get("AREA_GERAL")),
                    "nivel": self._text(row.get("TP_NIVEL_ACADEMICO") or row.get("NIVEL")),
                    "grau": self._text(row.get("TP_GRAU_ACADEMICO") or row.get("GRAU")),
                    "modalidade": self._text(row.get("TP_MODALIDADE_ENSINO") or row.get("MODALIDADE")),
                },
                ["co_curso", "co_ies"],
            )
            curso_id = self.db.execute(
                select(DimCurso.id).where(DimCurso.co_curso == co_curso, DimCurso.co_ies == co_ies)
            ).scalar_one()

            self.db.add(
                FatoIndicadores(
                    ano=ano,
                    co_ies=co_ies,
                    curso_id=curso_id,
                    qt_vaga=self._int_or_zero(row.get("QT_VAGA")),
                    qt_ing=self._int_or_zero(row.get("QT_ING")),
                    qt_mat=self._int_or_zero(row.get("QT_MAT")),
                    qt_conc=self._int_or_zero(row.get("QT_CONC")),
                    qt_sit_trancada=self._int_or_zero(row.get("QT_SIT_TRANCADA")),
                    qt_sit_desvinculado=self._int_or_zero(row.get("QT_SIT_DESVINCULADO")),
                    qt_sit_transferido=self._int_or_zero(row.get("QT_SIT_TRANSFERIDO")),
                    qt_perda=self._int_or_zero(row.get("QT_PERDA")),
                )
            )

        self.db.commit()

    def _upsert(self, model: type, values: dict[str, Any], index_elements: list[str]) -> None:
        stmt = insert(model).values(**values)
        update_values = {
            key: getattr(stmt.excluded, key)
            for key in values
            if key not in index_elements
        }
        if update_values:
            stmt = stmt.on_conflict_do_update(index_elements=index_elements, set_=update_values)
        else:
            stmt = stmt.on_conflict_do_nothing(index_elements=index_elements)
        self.db.execute(stmt)

    @staticmethod
    def _text(value: Any) -> str | None:
        if value is None:
            return None
        text = str(value).strip()
        return text or None

    @classmethod
    def _int_or_zero(cls, value: Any) -> int:
        return cls._int_or_none(value) or 0

    @staticmethod
    def _int_or_none(value: Any) -> int | None:
        if value is None or value == "":
            return None
        try:
            return int(float(value))
        except (TypeError, ValueError):
            return None

    def _co_curso(self, row: dict[str, Any]) -> int:
        co_curso = self._int_or_none(row.get("CO_CURSO"))
        if co_curso is not None:
            return co_curso
        base = f"{row.get('CO_IES', '')}|{row.get('NO_CURSO', '')}".encode("utf-8")
        return zlib.crc32(base)
