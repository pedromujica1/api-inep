from etl.layouts.layout_2003 import ETL2003


class ETL2007(ETL2003):
    ano = 2007
    descricao_layout = "layout_2007"

    def transformar(self):
        raise NotImplementedError("Mapeamento especifico de 2007 ainda precisa ser preenchido")
