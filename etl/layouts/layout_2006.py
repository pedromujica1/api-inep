from etl.layouts.layout_2003 import ETL2003


class ETL2006(ETL2003):
    ano = 2006
    descricao_layout = "layout_2006"

    def transformar(self):
        raise NotImplementedError("Mapeamento especifico de 2006 ainda precisa ser preenchido")
