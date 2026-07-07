from pathlib import Path

from etl.base import BaseETL
from etl.layouts import ETL2003, ETL2004, ETL2005, ETL2006, ETL2007, ETL2008, ETLModerno


class ETLFactory:
    @staticmethod
    def criar(ano: int, origem: Path | None = None) -> BaseETL:
        layouts = {
            2003: ETL2003,
            2004: ETL2004,
            2005: ETL2005,
            2006: ETL2006,
            2007: ETL2007,
            2008: ETL2008,
        }
        if ano in layouts:
            return layouts[ano](origem=origem)
        if 2009 <= ano <= 2024:
            return ETLModerno(ano=ano, origem=origem)
        raise ValueError("Ano suportado: 2003 a 2024")
