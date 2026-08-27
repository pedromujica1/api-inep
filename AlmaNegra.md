# Trabalho — Pirata Alma Negra

**Professor:** Prof. Me. Matheus Raffael Simon

---

## Contexto — O Alma Negra

Atenção marujo! O pirata Alma Negra está vagando em sua direção e seu objetivo é lhe impedir de seguir nessa jornada.

A batalha é iminente, então se prepare para enfrentar este pirata.

Para derrotá-lo, cada marujo deverá resolver os exercícios a seguir.

---

# Exercício 1 — Banco de Dados da Frota

O Capitão Barba de Byte está organizando a maior frota pirata dos Sete Mares.

Depois de anos registrando suas batalhas em mapas velhos, pedaços de pergaminho e até em garrafas, ele percebeu que estava ficando impossível controlar todas as informações sobre seus:

- Navios;
- Capitães;
- Tripulações;
- Armamentos;
- Batalhas.

Por isso, decidiu contratar um especialista, o Juquinha, para criar um **Banco de Dados Pirata**, capaz de armazenar todas as informações da frota e das batalhas realizadas.

Durante uma reunião a bordo do navio Pérola do Banco de Dados, o Capitão Barba de Byte explicou a Juquinha todas as regras que deverão ser consideradas.

### Piratas

A frota possui vários piratas e algumas informações sobre eles deverão obrigatoriamente ser armazenadas.

Cada pirata deverá possuir:

- Nome;
- Apelido pirata, que deverá ser único;
- Data de nascimento;
- Função dentro da tripulação;
- Data de cadastro.

Os piratas poderão ser classificados em dois tipos:

- Capitão;
- Tripulante.

Essa classificação deverá ser armazenada no banco de dados.

Também poderão ser cadastradas algumas informações adicionais sobre cada pirata:

- Observação;
- Ilha ou cidade de origem.

Um pirata poderá possuir várias habilidades, como:

- Navegação;
- Combate com espada;
- Operação de canhões;
- Manutenção do navio.

Uma mesma habilidade poderá pertencer a vários piratas.

---

### Portos

Durante suas aventuras, a frota utiliza diversos portos.

Para cada porto deverão ser armazenadas obrigatoriamente:

- Nome do porto;
- Ilha ou cidade;
- Região marítima;
- País ou reino ao qual pertence.

Também poderão ser armazenadas outras informações, como:

- Descrição do porto;
- Observações sobre os perigos encontrados no local.

Cada navio deverá possuir um **porto de origem**.

Nenhuma informação numérica utilizada para indicar a capacidade de um porto poderá possuir valores negativos.

---

### Navios

A frota do Capitão Barba de Byte possui vários navios.

Cada navio deverá possuir obrigatoriamente:

- Nome;
- Código de identificação;
- Data de construção;
- Capacidade máxima de tripulantes;
- Quantidade de canhões;
- Porto de origem.

Regras:

- O código do navio deverá ser único.
- A capacidade de tripulantes não poderá possuir valores negativos.
- A quantidade de canhões não poderá possuir valores negativos.
- Cada navio deverá possuir um capitão responsável.
- Um capitão poderá comandar diferentes navios ao longo das aventuras da frota.

---

### Batalhas

O principal objetivo do sistema será registrar as batalhas realizadas pela frota.

Cada batalha deverá possuir obrigatoriamente:

- Número de identificação, que deverá ser único;
- Data da batalha;
- Navio participante;
- Capitão responsável;
- Local da batalha;
- Estratégia principal utilizada;
- Valor do tesouro conquistado.

#### Regras

- Se o usuário não inserir a data da batalha, deverá ser utilizada a data do dia.
- Nenhum valor de tesouro poderá ser negativo.
- Durante uma batalha, também poderá ser registrado um valor destinado aos reparos do navio.
- O valor destinado aos reparos não poderá ser superior a **50 moedas de ouro**.
- Também deverão ser armazenadas:
  - Observação sobre a batalha;
  - Quantidade de dias necessária para o navio retornar ao porto.
- O retorno ao porto deverá ocorrer em um prazo máximo de **30 dias após a batalha**.

#### Estratégias permitidas

As estratégias principais permitidas serão:

- Canhões;
- Abordagem;
- Emboscada.

O capitão responsável pela batalha também deverá:

- Estar devidamente cadastrado no banco de dados;
- Estar vinculado à batalha.

---

### Armamentos

Os navios poderão utilizar diversos armamentos durante uma batalha.

Cada armamento deverá possuir obrigatoriamente:

- Descrição;
- Código;
- Peso;
- Poder de ataque.

#### Regras

- O peso deverá possuir valor positivo.
- O poder de ataque deverá possuir valor positivo.

Quando um armamento for utilizado em uma batalha, deverão ser armazenadas também:

- Quantidade utilizada;
- Quantidade de disparos ou utilizações;
- Dano causado.

Todas as informações relacionadas ao uso de um armamento em uma batalha deverão ser obrigatórias.

Uma batalha poderá utilizar vários armamentos e um mesmo armamento poderá ser utilizado em várias batalhas.

---

# Exercício 2 — Registro Oficial da Batalha

Depois de cada grande confronto, o Capitão Barba de Byte exige a criação de um **Registro Oficial da Batalha**.

Esse registro deverá:

- Existir no banco de dados;
- Possuir vínculo com uma batalha.

Entretanto, o capitão não informou exatamente quais informações deverão existir nesse registro.

Dessa forma, o responsável pelo desenvolvimento deverá definir quais atributos considera necessários para armazenar adequadamente as informações de um **Registro Oficial da Batalha**.

---

# Exercício 3 — DER, DDL e DML

Como os piratas não conhecem praticamente nada sobre Banco de Dados, Juquinha será responsável por interpretar todas essas regras e construir o sistema.

Deverá ser criado o:

- **Diagrama Entidade-Relacionamento (DER)** completo da solução.

Após a criação do DER, deverão ser desenvolvidas todas as instruções SQL necessárias para criar a estrutura do banco de dados.

Também deverão ser realizados:

- No mínimo **3 INSERTs para cada tabela criada**.

Os dados inseridos deverão permitir que **todas as consultas solicitadas posteriormente retornem algum resultado**.

---

# Exercício 4 — Alterações e Consulta

Após criar o banco de dados, realize as seguintes tarefas utilizando SQL:

### 4.1 — Renomear tabela

Crie uma SQL para alterar o nome da tabela:

`capitao`

para:

`comandante`

### 4.2 — Restrição na observação

Adicione uma restrição que não permita que a **observação da batalha** seja vazia.

### 4.3 — Nova coluna

Adicione uma nova coluna à tabela:

`pirata`

### 4.4 — Recompensa do comandante

Crie um campo chamado:

`recompensa`

para o comandante.

Regras:

- Não deverá aceitar valores abaixo de **1.621 moedas de ouro**.
- Caso nenhum valor seja informado durante o cadastro, deverá ser armazenado automaticamente o valor de **1.621 moedas de ouro**.

### 4.5 — Renomear coluna

Altere o nome da coluna:

`recompensa`

para:

`pagamento_comandante`

### 4.6 — Batalhas por comandante

Crie uma consulta que mostre **quantas batalhas cada comandante realizou**.

---

# Exercício 5 — Consultas SQL

Realize as seguintes consultas utilizando SQL:

### 5.1 — Maior tesouro por navio

Retorne o **maior valor de tesouro conquistado por cada navio**.

### 5.2 — Média dos tesouros

Retorne a **média dos valores dos tesouros conquistados nas batalhas**.

### 5.3 — Menor tesouro

Retorne o **Registro Oficial da Batalha correspondente à batalha que conquistou o menor valor de tesouro**.

### 5.4 — Batalhas no primeiro trimestre de 2026

Retorne todas as batalhas realizadas no **primeiro trimestre de 2026**.

### 5.5 — Batalhas com estratégia Canhões

Retorne:

- Número da batalha;
- Valor do tesouro conquistado;

para as batalhas em que a estratégia utilizada foi:

`Canhões`

---

# Entrega

**Data:** 20/08/2026

**Modalidade:** Individual

**Horário:** Horário da aula

Cada pergunta deverá ser entregue em um arquivo `.txt` contendo todas as SQL:

- DDLs;
- DMLs;
- DQLs.

Também deverá ser entregue:

- DER do Visual Paradigm (`.vvp`);
- Uma imagem do DER.

**Forma de entrega:** Teams.
