from etl.layouts.layout_2003 import ETL2003


class ETL2004(ETL2003):
    ano = 2004
    descricao_layout = "layout_2004"

    def transformar(self):
        raise NotImplementedError("Mapeamento especifico de 2004 ainda precisa ser preenchido")
