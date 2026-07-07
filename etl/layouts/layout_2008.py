from etl.layouts.layout_2003 import ETL2003


class ETL2008(ETL2003):
    ano = 2008
    descricao_layout = "layout_2008"

    def transformar(self):
        raise NotImplementedError("Mapeamento especifico de 2008 ainda precisa ser preenchido")
