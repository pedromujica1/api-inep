

# Resumo de Comandos SQL — Trabalho: Pirata Alma Negra

## 1. Linguagem de Definição de Dados (DDL)

### Criar Tabelas (`CREATE TABLE`)

Usado para definir as tabelas, seus tipos de dados e restrições básicas (como chaves primárias e estrangeiras).

```sql
CREATE TABLE nome_tabela (
    coluna1 tipo_dado restricao,
    coluna2 tipo_dado,
    PRIMARY KEY (coluna1),
    FOREIGN KEY (coluna2) REFERENCES outra_tabela(coluna_ref)
);

```

### Restrições Básicas (Constraints) úteis para o trabalho:

* **Não permitir nulos:** `NOT NULL`
* **Valor padrão automático:** `DEFAULT valor`
* **Garantir valores válidos (ex: sem números negativos ou limites):** `CHECK (coluna > 0)`
* **Garantir valor único:** `UNIQUE (coluna)`
* **Chave Primária:** `PRIMARY KEY (coluna)`
* **Chave Estrangeira com ações em cascata/padrão:**
```sql
FOREIGN KEY (coluna_fk) REFERENCES tabela_ref(coluna_pk) 
ON DELETE SET DEFAULT 
ON UPDATE CASCADE

```



### Alterar Estruturas (`ALTER TABLE`)

* **Alterar o nome de uma tabela:**
```sql
ALTER TABLE capitao RENAME TO comandante;

```


* **Adicionar uma nova coluna:**
```sql
ALTER TABLE pirata ADD COLUMN nova_coluna tipo_dado;

```


* **Adicionar restrição (ex: `CHECK` para evitar observação vazia):**
```sql
ALTER TABLE batalha ADD CONSTRAINT chk_obs CHECK (observacao IS NOT NULL AND observacao <> '');

```


* **Adicionar coluna com valor `DEFAULT` e restrição de valor mínimo (ex: `recompensa` para comandante):**
```sql
ALTER TABLE comandante ADD COLUMN recompensa DECIMAL(10,2) DEFAULT 1621 CHECK (recompensa >= 1621);

```


* **Renomear uma coluna:**
```sql
ALTER TABLE comandante RENAME COLUMN recompensa TO pagamento_comandante;

```



---

## 2. Linguagem de Manipulação de Dados (DML)

### Inserir Dados (`INSERT INTO`)

Usado para popular as tabelas com os dados iniciais (mínimo de 3 por tabela):

```sql
INSERT INTO nome_tabela (coluna1, coluna2) 
VALUES ('valor1', 123);

```

---

## 3. Linguagem de Consulta de Dados (DQL)

### Estrutura Básica de Consulta (`SELECT`)

```sql
SELECT coluna1, coluna2
FROM tabela1, tabela2
WHERE condicao;

```

### Renomear Atributos ou Tabelas (`AS`)

```sql
SELECT coluna AS novo_nome
FROM tabela AS t;

```

### Junções de Tabelas (`JOIN`)

Para cruzar informações entre várias tabelas relacionadas:

```sql
SELECT t1.coluna, t2.coluna
FROM tabela1 AS t1
INNER JOIN tabela2 AS t2 ON t1.id = t2.id_t1;

```

### Funções de Agregação (Para contagens, máximos e médias)

* **Contar registros (ex: quantas batalhas cada comandante realizou):**
```sql
SELECT id_comandante, COUNT(*) AS total_batalhas
FROM batalha
GROUP BY id_comandante;

```


* **Encontrar o maior valor (ex: maior tesouro por navio):**
```sql
SELECT id_navio, MAX(valor_tesouro) AS maior_tesouro
FROM batalha
GROUP BY id_navio;

```


* **Calcular a média (ex: média dos tesouros):**
```sql
SELECT AVG(valor_tesouro) AS media_tesouros
FROM batalha;

```



### Filtros por Período e Texto (`WHERE`, `BETWEEN`, `LIKE`)

* **Filtrar por intervalo de datas (ex: primeiro trimestre de 2026):**
```sql
SELECT *
FROM batalha
WHERE data_batalha BETWEEN '2026-01-01' AND '2026-03-31';

```


* **Filtrar por texto exato (ex: estratégia igual a "Canhões"):**
```sql
SELECT *
FROM batalha
WHERE estrategia_principal = 'Canhões';

```



### Subconsultas (Subqueries)

Útil para retornar registros com base em condições extremas (ex: o Registro Oficial da Batalha com o menor tesouro):

```sql
SELECT *
FROM registro_oficial
WHERE id_batalha = (
    SELECT id_batalha 
    FROM batalha 
    ORDER BY valor_tesouro ASC 
    LIMIT 1
);

```


Aqui está o resumo em Markdown focado estritamente nos conceitos e comandos DDL abordados no documento, ideais para estruturar o banco de dados do trabalho:

---

# Resumo DDL (Data Definition Language)

## 1. O que é o DDL?

* A Linguagem de Definição de Dados define o nível lógico de um banco de dados.


* É utilizada para **criar** o banco de dados e tabelas, **alterar** estruturas e **deletar** elementos (como bancos e tabelas).



---

## 2. Tipos de Dados em SQL (PostgreSQL)

* **Numéricos:**
* `smallint` (2 bytes), `integer` (4 bytes), `bigint` (8 bytes).


* `numeric` / `decimal`: Precisão especificada pelo usuário, ideal para cálculos exatos e valores monetários (suporta até 1000 dígitos).


* `real` (4 bytes) e `double` (8 bytes): Valores de ponto flutuante de precisão variável.


* `serial` (4 bytes) e `bigserial` (8 bytes): Não são tipos de dados puros, mas notações para criar identificadores únicos de **auto-incremento** inteiros.




* **Cadeia de Caracteres:**
* `varchar(n)` / `character varying(n)`: Tamanho variável com limite.


* `char(n)` / `character(n)`: Tamanho fixo (preenchido com espaços em branco).


* `text`: Tamanho ilimitado.




* **Data e Hora:**
* `date`: Armazena somente a data (4 bytes).


* `timestamp`: Data e hora (com ou sem fuso horário).


* `time`: Somente hora (com ou sem fuso horário).


* `interval`: Intervalo de tempo (16 bytes).




* **Outros:**
* `boolean`: Armazena estados de verdadeiro ou falso (1 byte).





---

## 3. Comandos de Criação (`CREATE`)

### Criar Banco de Dados

```sql
CREATE DATABASE nome_do_banco
WITH OWNER = postgres
ENCODING = 'UTF8'
TABLESPACE = pg_default
CONNECTION LIMIT = -1;

```

### Criar Tabelas (`CREATE TABLE`)

Utilizado para especificar uma nova relação (tabela da base), definindo nomes de atributos, seus tipos (domínios), restrições iniciais (`NOT NULL`, chaves e integridade).

```sql
CREATE TABLE nome_tabela (
    coluna1 varchar(80),
    coluna2 int, -- Exemplo de comentário com dois traços
    coluna3 real,
    coluna4 date
);

```

* **Nota sobre sintaxe:** Espaços em branco, tabulações e quebras de linha são livres em comandos SQL. Comentários de linha única são iniciados por dois traços (`--`).

Aqui está o resumo em Markdown focado nos conceitos e comandos de DDL (Parte 2) abordados no documento, essenciais para a criação, modelagem e alteração das tabelas do trabalho:

---

# Resumo DDL — Chaves, Restrições e Modificação de Tabelas

## 1. Chaves Primárias e Estrangeiras

### Chave Primária (`PRIMARY KEY`)

* Identificador único da tabela; cada registro possui uma e apenas uma.


* Não pode receber valores nulos (`NOT NULL` implícito).


* Normalmente auto-incrementada pelo banco (ex: tipo `SERIAL` no PostgreSQL).


* Exemplo de criação com auto-incremento:


```sql
CREATE TABLE pessoa (
    Id_pessoa SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    Endereco VARCHAR(100),
    Cidade VARCHAR(100)
);

```



### Chave Estrangeira (`FOREIGN KEY`)

* Estabelece o relacionamento entre tabelas, fazendo referência à chave primária de outra tabela.


* Pode ser nula (o que pode gerar registros órfãos) ou múltipla (uma tabela pode ter zero ou várias chaves estrangeiras).


* Exemplo de definição e restrição de FK:


```sql
CREATE TABLE Carro (
    ID_Carro SERIAL PRIMARY KEY,
    Nome VARCHAR(255),
    Marca VARCHAR(255),
    ID_Pessoa INTEGER,
    CONSTRAINT fk_PesCarro FOREIGN KEY (ID_Pessoa) REFERENCES Pessoa (ID_Pessoa)
);

```



---

## 2. Modificação de Tabelas (`ALTER TABLE`)

Permite alterar a estrutura da tabela sem precisar recriá-la do zero.

### Adicionar e Remover Colunas

* Adicionar coluna:


```sql
ALTER TABLE Produto ADD COLUMN descricao TEXT;
-- Com restrição opcional:
ALTER TABLE Produto ADD COLUMN descricao TEXT CHECK (descricao <> '');

```


* Remover coluna:


```sql
ALTER TABLE Produto DROP COLUMN descricao;
-- Para apagar em cascata (caso haja dependências):
ALTER TABLE Produto DROP COLUMN descricao CASCADE;

```



### Adicionar e Remover Restrições (`Constraints`)

* Adicionar restrições:


```sql
ALTER TABLE Produto ADD CHECK (nome <> '');
ALTER TABLE Produto ADD CONSTRAINT nome_restricao UNIQUE (produto_num);
ALTER TABLE Produto ADD FOREIGN KEY (produto_grupo_id) REFERENCES produto_grupo;
ALTER TABLE Produto ALTER COLUMN produto_num SET NOT NULL;

```


* Remover restrições:


```sql
ALTER TABLE Produto DROP CONSTRAINT nome_restricao;
-- Para remover NOT NULL:
ALTER TABLE Produto ALTER COLUMN produto_num DROP NOT NULL;

```



### Modificar Valores Padrão (`DEFAULT`)

* Adicionar ou alterar valor padrão:


```sql
ALTER TABLE Produto ALTER COLUMN preco SET DEFAULT 7.77;

```


* Remover valor padrão:


```sql
ALTER TABLE Produto ALTER COLUMN preco DROP DEFAULT;

```



### Modificar Tipos de Dados e Renomear

* Alterar o tipo de dado de uma coluna:


```sql
ALTER TABLE Produto ALTER COLUMN preco TYPE NUMERIC;

```


* Renomear uma coluna:


```sql
ALTER TABLE Produto RENAME COLUMN produto_num TO produto_numero;

```


* Renomear uma tabela:


```sql
ALTER TABLE Produto RENAME TO itens;

```



---

## 3. Comandos de Exclusão e Limpeza

* **`TRUNCATE TABLE`**: Remove todas as linhas de uma tabela de forma rápida e eficiente (sem usar `WHERE`, sem registrar exclusões individuais).


```sql
TRUNCATE TABLE nome_tabela;

```


* **`DROP TABLE`**: Descarta/apaga uma tabela existente (não permitindo se estiver referenciada ou contiver dados dependendo da configuração).


```sql
DROP TABLE nome_tabela;

```


* **`DROP DATABASE`**: Elimina um banco de dados existente.


```sql
DROP DATABASE databasename;

```

Aqui está o resumo em Markdown focado nos conceitos e comandos de restrições (Constraints) abordados no documento, complementando a parte DDL para resolver o trabalho:

---

# Resumo DDL — Restrições (Constraints) Avançadas

## 1. O que são Restrições?

* São regras aplicadas a colunas ou tabelas para garantir maior controle, integridade e validação dos dados.


* Caso um usuário tente inserir um dado que viole uma restrição, o SGBD interrompe a operação e gera um erro.



---

## 2. Tipos de Restrições

### Restrição `CHECK`

* É o tipo mais genérico de restrição; exige que o valor de uma coluna satisfaça uma expressão booleana (verdadeira).


* Pode ser aplicada a uma ou múltiplas colunas.


* É altamente recomendável nomear as restrições com a palavra-chave `CONSTRAINT` para facilitar a identificação de erros e manutenções:


```sql
CREATE TABLE Produto (
    produto_num INTEGER,
    nome TEXT,
    preco NUMERIC CONSTRAINT preco_positivo CHECK (preco > 0),
    preco_desconto NUMERIC,
    CONSTRAINT preco_desconto_positivo CHECK (preco_desconto > 0),
    CONSTRAINT desconto_valido CHECK (preco > preco_desconto)
);

```



### Restrição `NOT NULL`

* Especifica que uma coluna não pode assumir valores nulos (`NULL`).


```sql
CREATE TABLE Produto (
    produto_num INTEGER NOT NULL,
    nome TEXT NOT NULL
);

```



### Restrição `UNIQUE`

* Garante que os dados inseridos em um campo (ou grupo de campos) sejam únicos em comparação com todas as outras tuplas da tabela.


```sql
CREATE TABLE Produto (
    produto_num INTEGER UNIQUE,
    nome TEXT NOT NULL UNIQUE
);

```



### Chaves Primárias (`PRIMARY KEY`)

* A chave primária é uma combinação de uma restrição `UNIQUE` e uma `NOT NULL`.


* Automaticamente cria um índice do tipo `btree` na(s) coluna(s) correspondente(s).


* Pode ser simples ou **composta** (envolvendo mais de uma coluna):


```sql
CREATE TABLE Exemplo (
    a INTEGER,
    b INTEGER,
    c INTEGER,
    PRIMARY KEY (a, c)
);

```



### Chaves Estrangeiras (`FOREIGN KEY`)

* Garante a **integridade referencial**, especificando que os valores em uma coluna (ou grupo de colunas) devem corresponder aos valores existentes em outra tabela (geralmente na chave primária dela).


* O número e o tipo de dados das colunas referenciadas devem corresponder exatamente.


```sql
CREATE TABLE Pedido (
    pedido_num INTEGER PRIMARY KEY,
    produto_num INTEGER REFERENCES produto (produto_num),
    qtd INTEGER
);

```



---

## 3. Representação de Cardinalidades em DDL

* **Relacionamento 1:1 (Um para Um):**
A chave primária da tabela dependente também atua como chave estrangeira apontando para a tabela principal (geralmente associada a uma restrição `UNIQUE`).


```sql
CREATE TABLE Pessoas (
    pessoa_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL
);

CREATE TABLE Documentos (
    documento_id INT PRIMARY KEY,
    numero_passaporte VARCHAR(20) UNIQUE NOT NULL,
    FOREIGN KEY (documento_id) REFERENCES Pessoas (pessoa_id)
);

```


* **Relacionamento 1:N / N:N (Muitos para Muitos via Tabela Associativa):**
Uso de chaves primárias compostas formadas pelas chaves estrangeiras das entidades envolvidas.


```sql
CREATE TABLE Cursos (
    curso_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE Alunos (
    aluno_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE Inscricoes (
    curso_id INT NOT NULL,
    aluno_id INT NOT NULL,
    data_inscricao DATE NOT NULL,
    PRIMARY KEY (curso_id, aluno_id),
    FOREIGN KEY (curso_id) REFERENCES Cursos(curso_id),
    FOREIGN KEY (aluno_id) REFERENCES Alunos(aluno_id)
);

```

Aqui está o resumo em Markdown focado nos conceitos e comandos de DML (`INSERT`) e importação/exportação (`COPY`) abordados no documento:

---

# Resumo DML — Comando INSERT e Importação de Dados (COPY)

## 1. O Comando `INSERT`

* Utilizado para criar e inserir novas linhas (tuplas) em uma tabela.


* A ordem dos campos declarados deve corresponder exatamente à ordem dos valores passados.


* Valores que não sejam numéricos simples (como strings, textos e datas) devem ser inseridos entre aspas simples (`'`).



### Exemplos de Utilização do `INSERT`

* **Inserção especificando colunas:**
```sql
INSERT INTO ATOR (nome, sobrenome) 
VALUES ('Peter', 'Dinklage');

```


* **Inserção omitindo nomes de colunas** (os valores seguem a ordem de criação da tabela; pode-se usar `DEFAULT` para colunas auto-incrementais ou com valores padrão):


```sql
INSERT INTO ATOR 
VALUES (DEFAULT, 'Lena', 'Headey');

```


* **Inserção de múltiplas linhas em um único comando:**
```sql
INSERT INTO IDIOMA (nome) 
VALUES ('Francês'),
       ('Italiano'),
       ('Japonês'),
       ('Chinês'),
       ('Espanhol');

```



---

## 2. O Comando `COPY`

* Utilizado para mover grandes massas de dados entre tabelas do PostgreSQL e arquivos externos padronizados.


* `COPY FROM`: Copia dados de um arquivo externo para dentro de uma tabela.


* `COPY TO`: Copia/exporta o conteúdo de uma tabela para um arquivo externo.



### Opções Comuns do `COPY`

* `NULL '*'` : Especifica a string que representa um valor nulo no arquivo.


* `CSV` : Indica que o arquivo está no formato CSV.


* `CSV HEADER` : Indica que a primeira linha do arquivo é um cabeçalho com os nomes das colunas e deve ser ignorada.


* `DELIMITER` : Permite definir um caractere separador de campos diferente da vírgula padrão (ex: `;` ou `|`).



### Exemplos de Uso do `COPY`

* **Importar dados de um arquivo de texto (`COPY FROM`)** com delimitador de vírgula:


```sql
COPY ATOR (nome, sobrenome)
FROM '/tmp/atores.txt'
DELIMITER ',';

```


* **Exportar dados de uma tabela para um arquivo (`COPY TO`)** separando os campos por barra vertical (`|`):


```sql
COPY ATOR (nome, sobrenome)
TO '/tmp/atores2.txt'
DELIMITER '|';

```

Aqui está o resumo em Markdown focado nos comandos DML de atualização (`UPDATE`) e exclusão (`DELETE`) abordados no documento:

---

# Resumo DML — Comandos UPDATE e DELETE

## 1. O Comando `UPDATE`

* Utilizado para atualizar uma ou mais linhas já existentes em uma tabela.


* É fundamental o uso da cláusula `WHERE` para delimitar os registros afetados; caso contrário, **todos os registros** da tabela serão modificados.



### Sintaxe e Exemplo de Uso

* Sintaxe básica:


```sql
UPDATE Tabela_Alvo
SET coluna = <novo valor>,
    <outra_coluna> = <novo valor>
WHERE <condição>;

```


* Exemplo prático de atualização:


```sql
UPDATE CATEGORIA
SET NOME = 'Comédia Romântica'
WHERE NOME LIKE 'Comédia';

```



---

## 2. O Comando `DELETE`

* Utilizado para remover uma ou mais linhas existentes em uma tabela.


* Assim como no `UPDATE`, a ausência da cláusula `WHERE` fará com que **todos os registros** da tabela sejam apagados, causando perda massiva de dados.



### Sintaxe e Exemplo de Uso

* Sintaxe básica:


```sql
DELETE FROM Tabela_Alvo 
WHERE <condição>;

```


* Exemplo prático de remoção:


```sql
DELETE FROM CATEGORIA 
WHERE nome LIKE 'Comédia %';

```
Aqui está o resumo em Markdown focado nos conceitos e comandos de consultas (`DQL` / `SELECT`) abordados no documento:

---

# Resumo DQL — Comando SELECT e Consultas

## 1. Estrutura Básica do Comando `SELECT`

* O comando responsável por obter e retornar dados em um banco de dados é a consulta (*query*).


* Sintaxe básica:


```sql
SELECT Lista_seleção 
FROM Expressão_Table 
[Filtros] 
[Agrupamentos] 
[Ordenação];

```


* Exemplos simples de uso:


```sql
SELECT 4 * 5;
SELECT 'EXEMPLO QUERY';
SELECT * FROM ATOR;

```



---

## 2. Cláusula `FROM` e Seleção de Campos

* A cláusula `FROM` especifica a origem dos dados (tabelas, subqueries ou junções/`JOIN`).


* A lista de seleção pode conter colunas específicas, cálculos ou o asterisco (`*`) para retornar todos os campos.


```sql
SELECT titulo, descricao FROM Filme;
SELECT titulo, descricao, (2 * taxa) FROM Filme;

```



---

## 3. Ordenação (`ORDER BY`)

* Utilizada para ordenar a tabela de saída com base nos valores de uma ou mais colunas.


* Por padrão, ordena em ordem ascendente (`ASC`). Para ordem descendente, utiliza-se o termo `DESC`.


```sql
SELECT * FROM ATOR ORDER BY nome DESC;
SELECT * FROM ATOR ORDER BY nome ASC;

```



---

## 4. Filtros (`WHERE`)

* Define condições booleanas para filtrar as linhas geradas pelo `FROM`. Linhas que retornam `TRUE` são mantidas; `FALSE` ou `NULL` são descartadas.


```sql
SELECT * FROM Filme WHERE taxa <= 10;

```



### Operadores Especiais no `WHERE`

* **`LIKE` (Comparação de textos e padrões):**
* `WHERE nome LIKE 'Emilia'` (Igual a 'Emilia')


* `WHERE nome LIKE 'Emi%'` (Iniciado por 'Emi')


* `WHERE nome LIKE 'E%'` (Iniciado pela letra 'E')


* `WHERE nome LIKE '%a%'` (Contém a letra 'a')




* **`BETWEEN` (Intervalos numéricos ou de datas):**
```sql
SELECT * FROM Filme WHERE taxa BETWEEN 5 AND 10;

```


* **`IN` (Lista de itens ou subqueries):**
```sql
SELECT * FROM Idioma WHERE nome IN ('Português', 'Inglês');
SELECT * FROM Filme WHERE Filme_id IN (1, 2);

```



---

## 5. Agrupamento (`GROUP BY`) e Funções de Agregação

* Utilizado para agrupar linhas que possuem os mesmos valores em determinadas colunas, eliminando redundâncias e permitindo o uso de funções estatísticas.



### Funções de Agregação Principais

* `AVG()`: Retorna a média.


* `COUNT()`: Retorna o número de linhas.


* `MAX()`: Retorna o maior valor.


* `MIN()`: Retorna o menor valor.


* `SUM()`: Retorna a soma dos valores.


* Exemplo de uso com `GROUP BY`:


```sql
SELECT filme_id, COUNT(ator_id) 
FROM ator_filme 
GROUP BY filme_id;

```



---

## 6. Restrição de Agrupamento (`HAVING`)

* Utilizada em conjunto com o `GROUP BY` para filtrar resultados de funções de agregação (já que o `WHERE` não pode ser aplicado diretamente sobre elas).


```sql
SELECT filme_id, COUNT(ator_id) 
FROM ator_filme 
GROUP BY filme_id 
HAVING COUNT(ator_id) > 1;

```



---

## 7. Paginação e Limite de Resultados (`LIMIT` e `OFFSET`)

* **`LIMIT`**: Restringe a quantidade máxima de linhas retornadas pela query.


```sql
SELECT * FROM ator_filme LIMIT 10;

```


* **`OFFSET`**: Pula uma determinada quantidade de linhas antes de iniciar o retorno dos dados.


```sql
SELECT * FROM ator_filme OFFSET 10;

```
Aqui está o resumo em Markdown focado nos conceitos avançados de agrupamento (`GROUP BY`) e filtragem pós-agregação (`HAVING`) abordados no documento:

---

# Resumo DQL — Group By e Having Avançados

## 1. A Cláusula `GROUP BY`

* Agrupa linhas de uma tabela com base em um ou mais atributos específicos e retorna uma tabela resumida, adicionando custo computacional à consulta.


* **Exemplo de agrupamento simples:**
```sql
SELECT genero, SUM(preco_pago) AS preco_total
FROM biblioteca
GROUP BY genero;

```



### Agrupamento de Múltiplas Colunas

* É possível agrupar os dados considerando mais de uma coluna simultaneamente.


```sql
SELECT formato, genero, SUM(preco_pago) AS preco_total
FROM biblioteca_expandida
GROUP BY formato, genero;

```



---

## 2. A Cláusula `HAVING`

* Utilizada para filtrar os resultados gerados após o agrupamento (`GROUP BY`) e o uso de funções de agregação (`SUM`, `AVG`, `COUNT`), funcionando como uma condição booleana sobre os dados agregados.


```sql
SELECT genero, SUM(preco_pago) AS preco_total
FROM biblioteca_expandida
GROUP BY genero
HAVING preco_total > 100;

```



---

## 3. Diferença entre `WHERE` e `HAVING`

* **`WHERE`**: Filtra os registros da tabela **antes** de qualquer agrupamento ou agregação.


* **`HAVING`**: Filtra os resultados **após** o agrupamento e o cálculo das funções de agregação.


* É permitido e comum utilizar `WHERE` e `HAVING` combinados na mesma consulta:


```sql
SELECT genero, SUM(preco_pago) AS preco_total
FROM biblioteca_expandida
WHERE preco_pago > 50
GROUP BY genero
HAVING preco_total > 100;

```

Aqui está o resumo em Markdown focado nos conceitos, regras e exemplos de subconsultas (`Subqueries`) e expressões relacionais abordados no documento:

---

# Resumo DQL — Subqueries e Expressões de Subconsulta

## 1. O que é uma Subquery?

* Uma subconsulta (*subquery*) é uma instrução SQL aninhada que relaciona dois conjuntos de resultados (*result sets*).


* É formada pela união de selects distintos através de operadores relacionais ou pela inclusão de selects com campos oriundos de mais de uma consulta.


* Como regra geral, a subconsulta deve retornar uma única coluna.



---

## 2. Exemplos de Utilização de Subqueries

* Seleção com função de agregação na subquery:


```sql
SELECT DISTINCT nom_curso,
       (SELECT MIN(dat_nasc) 
        FROM Alunos 
        WHERE Alunos.cod_curso = Cursos.cod_curso) AS Aluno_Mais_Velho
FROM Cursos;

```


* Filtragem baseada na ausência de registros (`NOT IN`):


```sql
SELECT D.nom_disc 
FROM DISCIPLINAS D
WHERE D.COD_DISC NOT IN (
    SELECT DISTINCT COD_DISC 
    FROM PRE_REQUISITOS
);

```



---

## 3. Expressões de Subquery (Retorno Booleano)

Expressões disponíveis em SQL que relacionam um campo da consulta principal com os resultados de uma subquery:

### `EXISTS`

* Avalia se a subconsulta retorna alguma linha; se retornar, resulta em `TRUE`, caso contrário, `FALSE`.


```sql
SELECT D.nom_disc 
FROM DISCIPLINAS D
WHERE EXISTS (
    SELECT 1 
    FROM PRE_REQUISITOS 
    WHERE COD_DISC = D.COD_DISC
);

```



### `IN` e `NOT IN`

* **`IN`**: Retorna `TRUE` se qualquer linha da subquery tiver valor não nulo e igual ao valor da query mãe.


* **`NOT IN`**: Retorna `TRUE` se todas as linhas da subquery forem diferentes dos valores da query mãe.



### `ANY` / `SOME`

* Compara as linhas da consulta principal com cada linha da subquery usando um operador lógico (ex: `= ANY`, `<> ANY`).


* Retorna `TRUE` se pelo menos uma comparação for verdadeira (`SOME` é sinônimo de `ANY`).


* *Nota:* As consultas abaixo são equivalentes:


```sql
SELECT D.nom_disc FROM DISCIPLINAS D WHERE D.COD_DISC IN (SELECT DISTINCT COD_DISC FROM PRE_REQUISITOS);
SELECT D.nom_disc FROM DISCIPLINAS D WHERE D.COD_DISC = SOME (SELECT DISTINCT COD_DISC FROM PRE_REQUISITOS);
SELECT D.nom_disc FROM DISCIPLINAS D WHERE D.COD_DISC = ANY (SELECT DISTINCT COD_DISC FROM PRE_REQUISITOS);

```



### `ALL`

* Compara os valores da query principal com **todos** os resultados retornados pela subquery.


* O `NOT IN` é semanticamente equivalente a `<> ALL`.


```sql
SELECT D.nom_disc 
FROM DISCIPLINAS D 
WHERE D.COD_DISC <> ALL (
    SELECT DISTINCT COD_DISC 
    FROM PRE_REQUISITOS
);

```
