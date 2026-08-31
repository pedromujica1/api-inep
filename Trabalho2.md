# Trabalho — Barbossa

**Professor:** Prof. Me. Matheus Raffael Simon

---

# Contexto — Hector Barbossa

Hector Barbossa é um terrível pirata, sempre acompanhado de seu PET chamado Gemini, conhecido por pegar coisas dos outros sem a devida permissão e entregar para Barbossa.

Certo dia, Barbossa convocou uma grande reunião pirata na misteriosa **Ilha da Caveira Quebrada**.

---

# Juquinha

O Pirata Juquinha recebeu uma mensagem secreta informando que o temido Capitão Barbossa convocou uma grande reunião pirata na misteriosa Ilha da Caveira Quebrada.

Piratas de diferentes tripulações estão chegando de várias partes dos sete mares para participar do encontro.

Cada capitão deverá registrar:

- Seu navio;
- Seus tripulantes;
- Os itens que levará para a reunião.

Juquinha conseguiu uma cópia dos registros do evento, mas as informações ainda precisam ser organizadas em um banco de dados.

Sua missão será ajudar Juquinha a organizar esses dados e descobrir informações importantes sobre os participantes da reunião.

---

# Exercício 1 — Diagrama Entidade-Relacionamento

Utilizando o **Visual Paradigm**, crie um **Diagrama Entidade-Relacionamento (DER)** contendo as seguintes entidades.

Defina corretamente:

- Chaves primárias;
- Chaves estrangeiras;
- Relacionamentos;
- Cardinalidades.

## Entidade — NAVIO

A tabela `NAVIO` deverá possuir:

| Campo |
|---|
| `id_navio` |
| `nome` |
| `quantidade_canhoes` |
| `capacidade` |
| `ano_fabricacao` |

## Entidade — PIRATA

A tabela `PIRATA` deverá possuir:

| Campo |
|---|
| `id_pirata` |
| `nome` |
| `apelido` |
| `idade` |
| `funcao` |
| `id_navio` |

## Entidade — ITEM

A tabela `ITEM` deverá possuir:

| Campo |
|---|
| `id_item` |
| `nome` |
| `tipo` |
| `valor` |
| `id_pirata` |

---

# Exercício 2 — DDL e Inserção de Dados

Com base no DER desenvolvido, escreva os comandos **DDL** necessários para criar as três tabelas:

- `NAVIO`
- `PIRATA`
- `ITEM`

## Alteração da tabela NAVIO

Barbossa decidiu que cada navio deverá informar também se possui autorização para participar da reunião.

Crie um campo do tipo:

`BOOLEAN`

A nomenclatura do campo deverá ser:

`autorizado`

## Inserção de dados

Cadastre:

- **3 navios**;
- **6 piratas**;
- **6 itens**.

Entre os dados cadastrados, deverão existir obrigatoriamente:

- Um navio chamado **Pérola Negra**;
- Um pirata chamado **Barbossa**;
- Um pirata chamado **Juquinha**;
- Pelo menos um navio com **mais de 20 canhões**;
- Itens com diferentes **valores** e **tipos**.

---

# Exercício 3 — UPDATE e DELETE

Ao chegar à Ilha da Caveira Quebrada, Juquinha percebeu que a quantidade de canhões do **Pérola Negra** foi cadastrada incorretamente.

### 3.1 — Atualização

Atualize a quantidade de canhões do Pérola Negra para:

`32`

### 3.2 — Exclusão

Um pirata chamado **Perneta** decidiu não participar mais da reunião.

Delete o registro desse pirata.

---

# Exercício 4 — Consultas SQL Básicas

Juquinha deve investigar a reunião.

Crie consultas para:

### a) Todos os piratas

Mostrar todos os piratas cadastrados.

### b) Nome e apelido

Mostrar somente:

- Nome;
- Apelido;

dos piratas cadastrados.

### c) Piratas com mais de 30 anos

Mostrar os piratas com idade:

`> 30`

### d) Piratas cujo nome começa com B

Mostrar os piratas cujo nome começa com a letra:

`B`

### e) Navios ordenados por quantidade de canhões

Mostrar os navios ordenados pela quantidade de canhões:

**Do maior para o menor.**

---

# Exercício 5 — Funções de Agregação

Juquinha quer saber quais são os itens mais valiosos que foram cadastrados.

Faça uso de **funções de agregação** para descobrir:

### a) Quantidade de itens

Quantos itens estão cadastrados?

### b) Maior valor

Qual é o item de maior valor?

### c) Valor médio

Qual é o valor médio dos itens cadastrados?

---

# Exercício 6 — GROUP BY e Subquery

Juquinha está com muito medo do que os outros piratas estão levando consigo.

### 6.1 — GROUP BY

Crie uma consulta para mostrar:

- O tipo do item;
- A quantidade de itens daquele tipo.

Utilize:

`GROUP BY`

### 6.2 — Quantidade maior que 3

Depois, Juquinha quer saber quais itens possuem uma quantidade maior que:

`3`

### 6.3 — Itens acima da média

Juquinha também quer descobrir quais itens possuem valor acima da média de todos os itens cadastrados.

Para isso, deverá ser criada uma:

**Subquery**

---

# Exercício 7 — Árgebria Refuncional

Antes de utilizar SQL para investigar os participantes da reunião, Juquinha encontrou algumas anotações escritas utilizando uma antiga linguagem utilizada pelos guardiões dos bancos de dados: a **Aritmética dos Sete Mares**, ou **Árgebria Refuncional**.

Os piratas, em sua maioria, eram analfabetos.

Utilizando as tabelas criadas para a reunião na Ilha da Caveira Quebrada, escreva as expressões em **Árgebria Refuncional** necessárias para representar as seguintes consultas:

### a) Piratas com mais de 30 anos

Encontrar todos os piratas que possuem idade maior que 30 anos.

### b) Nome e apelido dos piratas

Encontrar somente o nome e o apelido de todos os piratas cadastrados.

### c) Navios com mais de 20 canhões

Encontrar todos os navios que possuem mais de 20 canhões.

### d) Nome dos navios com mais de 20 canhões

Encontrar somente o nome dos navios que possuem mais de 20 canhões.

---

# Desfecho

Depois de organizar os registros, Juquinha finalmente consegue entender quem está participando da misteriosa reunião na Ilha da Caveira Quebrada.

Ele conhece os navios presentes, identifica os piratas registrados e descobre quais objetos valiosos foram levados para o encontro.

Barbossa observa Juquinha do outro lado da mesa e pergunta:

> — Como você conseguiu descobrir tudo isso?

Juquinha fecha seu notebook e responde:

> — Com SQL, capitão. Com SQL.

A reunião pode começar.

---

# Entrega

**Data:** 03/09/2026

**Modalidade:** Individual

**Horário:** Horário da aula.

Cada pergunta deverá ser entregue em um arquivo:

`.txt`

O arquivo deverá conter todas as SQL:

- DDLs;
- DMLs;
- DQLs.

O arquivo `.txt` deverá ser nomeado com o nome do aluno.

### Exemplo

`matheus_raffael_simon.txt`

Também deverá ser entregue:

- DER do Visual Paradigm (`.vvp`);
- Uma imagem do DER.

**Forma de entrega:** Teams.
