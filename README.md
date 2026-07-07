# api-inep

API para disponibilizar dados do Censo Superior do INEP para universidades estaduais do Parana.

## Arquitetura

O projeto foi organizado para a API consultar apenas o SQLite. Os CSVs entram somente no ETL:

```text
app/
|-- api/routes/              # rotas FastAPI enxutas
|-- db/models/               # DER SQLAlchemy
|-- db/repositories/         # consultas SQLAlchemy
|-- etl/                     # layouts, checkpoint e carga SQLite
|-- schemas/                 # contratos Pydantic
`-- services/                # regras do contrato do frontend
```

## Banco

Tabelas principais:

- `dim_ies`
- `dim_curso`
- `dim_ano`
- `fato_indicadores`
- `campos_disponiveis`
- `dim_layout`
- `etl_execucao`

Decisao aplicada: `dim_curso` possui chave interna `id` e unicidade por `(co_curso, co_ies)`, evitando ambiguidade entre cursos de IES diferentes.

## ETL

Fluxo implementado:

```text
CSV latin1 + separador detectado
-> filtro PR/Estadual/Universidade
-> normalizacao de colunas
-> padronizacao dos indicadores QT_*
-> checkpoint Parquet zstd
-> carga SQLite
```

Implementado agora:

- `ETL2003`: usa os somatorios das colunas antigas informadas no prompt.
- `ETLModerno`: atende 2009 a 2024 lendo `MICRODADOS_CADASTRO_CURSOS_{ano}.CSV`.
- `ETLFactory`: escolhe o layout pelo ano.
- `SQLiteLoader`: carrega dimensoes, fato e campos disponiveis.

Preparado, mas pendente de mapeamento:

- `ETL2004`
- `ETL2005`
- `ETL2006`
- `ETL2007`
- `ETL2008`

Esses anos ja possuem classes separadas para receberem as variacoes de colunas sem contaminar o layout de 2003 nem o layout moderno.

## API

Rota principal:

```http
POST /api/microdados/consultar
```

Exemplo de payload:

```json
{
  "anos": [2024],
  "indicadores": ["QT_ING", "QT_MAT"],
  "dimensao": "instituicao",
  "filtros": {
    "regiao": ["sul"]
  }
}
```

Dimensoes suportadas:

- `ano`
- `instituicao`
- `curso`
- `area`
- `area_geral`
- `modalidade`

Indicadores suportados:

- `QT_VAGA`
- `QT_ING`
- `QT_MAT`
- `QT_CONC`
- `QT_SIT_TRANCADA`
- `QT_SIT_DESVINCULADO`
- `QT_SIT_TRANSFERIDO`
- `QT_PERDA`

## Como rodar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Por padrao, o banco sera criado em `inep.sqlite3`.

Variaveis opcionais:

- `DATABASE_URL`: URL SQLAlchemy do banco.
- `INEP_DATA_DIR`: pasta base dos microdados.
- `INEP_CHECKPOINT_DIR`: pasta dos Parquets de checkpoint.

## Executar ETL por codigo

Antes de testar a API com dados reais, carregue o SQLite executando o ETL dos anos desejados.

### 2003

```python
from db.session import SessionLocal, init_db
from etl.runner import executar_etl

init_db()

with SessionLocal() as db:
    executar_etl(db, ano=2003, origem="/caminho/microdados_censo_da_educacao_superior_2003")
```

### 2009

```python
from db.session import SessionLocal, init_db
from etl.runner import executar_etl

init_db()

with SessionLocal() as db:
    executar_etl(db, ano=2009, origem="/caminho/microdados_censo_da_educacao_superior_2009")
```

### 2024

```python
from db.session import SessionLocal, init_db
from etl.runner import executar_etl

init_db()

with SessionLocal() as db:
    executar_etl(db, ano=2024, origem="/caminho/microdados_censo_da_educacao_superior_2024")
```

Para 2003, a pasta informada pode conter os CSVs diretamente ou um subdiretorio `DADOS`. Para 2009 a 2024, deve conter `MICRODADOS_CADASTRO_CURSOS_{ano}.CSV` diretamente ou em um subdiretorio `dados`.

## Direcionamentos pendentes

1. Confirmar os nomes reais das colunas de IES/curso nos arquivos de 2003. O loader aceita ausencias, mas quanto mais colunas existirem, melhor ficam as dimensoes.
2. Preencher os mapeamentos especificos de 2004 a 2008.
3. Validar se todos os anos modernos usam os mesmos codigos: `TP_ORGANIZACAO_ACADEMICA = 1`, `TP_CATEGORIA_ADMINISTRATIVA = 2`, `SG_UF = PR`.
4. Decidir se a API deve expor uma rota administrativa para disparar ETL ou se isso ficara apenas via script/CLI.
5. Depois de carregar 2003 e 2024, comparar totais agregados de `QT_ING`, `QT_MAT` e `QT_CONC` com os scripts exploratorios originais.
