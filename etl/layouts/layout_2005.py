from etl.layouts.layout_2003 import ETL2003


class ETL2005(ETL2003):
    ano = 2005
    descricao_layout = "layout_2005"

    def transformar(self):
        raise NotImplementedError("Mapeamento especifico de 2005 ainda precisa ser preenchido")
