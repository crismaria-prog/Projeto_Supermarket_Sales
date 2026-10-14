
# Supermarket Sales Analysis

Projeto de análise de dados de vendas de supermercado desenvolvido utilizando **Python, Pandas, PostgreSQL, SQL e Matplotlib**.

O projeto contempla desde a inspeção inicial dos dados até o processo de ETL, armazenamento em banco de dados, análises estatísticas e geração de gráficos.

---

## Objetivo

O objetivo do projeto é analisar um conjunto de dados de vendas de supermercado, aplicando conceitos de:

- análise exploratória de dados;
- SQL;
- banco de dados PostgreSQL;
- ETL;
- tratamento de dados com Pandas;
- estatística descritiva;
- visualização de dados;
- versionamento com Git e GitHub.

---

## Tecnologias utilizadas

- Python
- Pandas
- PostgreSQL
- SQL
- SQLAlchemy
- psycopg2
- python-dotenv
- Matplotlib
- DBeaver
- Git
- GitHub
- Visual Studio Code

---

## Estrutura do projeto

```text
Projeto_Supermarket_Sales/
│
├── data/
│   ├── raw/
│   │   └── SuperMarket Analysis.csv
│   │
│   └── processed/
│       └── vendas_tratadas.csv
│
├── resultados/
│   └── graficos/
│       ├── Faturamento_por_filial.png
│       ├── Faturamento_por_linha_de_produto.png
│       ├── Faturamento_por_mes.png
│       └── Vendas_por_forma_de_pagamento.png
│
├── sql/
│   ├── 01_criar_banco.sql
│   ├── 02_criar_tabelas.sql
│   └── 03_consultas.sql
│
├── src/
│   ├── 01_leitura_dados.py
│   ├── 02_etl_vendas.py
│   ├── 03_estatistica.py
│   └── 04_graficos.py
│
├── .env
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Dataset

O dataset utilizado contém informações sobre vendas realizadas por diferentes filiais de um supermercado.

O conjunto possui:

- **1000 registros**
- **17 colunas originais**

Entre as principais informações disponíveis estão:

- identificador da venda;
- filial;
- cidade;
- tipo de cliente;
- gênero;
- linha de produto;
- preço unitário;
- quantidade;
- imposto;
- valor total da venda;
- data;
- horário;
- forma de pagamento;
- custo da mercadoria;
- margem;
- receita bruta;
- avaliação do cliente.

Durante a inspeção inicial dos dados não foram identificados valores nulos, registros duplicados ou identificadores de venda duplicados.

---

## Banco de dados

Foi utilizado o PostgreSQL para armazenamento dos dados.

O banco criado para o projeto foi:

```text
supermarket_sales_db
```

Foram utilizadas duas tabelas principais:

### raw_vendas

Tabela responsável por armazenar os dados originais.

Os dados são mantidos o mais próximo possível do arquivo de origem, preservando os valores antes das transformações realizadas pelo ETL.

### vendas_tratadas

Tabela que recebe os dados após o processo de transformação e validação.

Ela possui tipos de dados adequados para cada informação, além de restrições como:

- chave primária;
- campos obrigatórios;
- validações numéricas;
- limites para avaliação.

---

## Processo ETL

O processo de ETL foi desenvolvido no arquivo:

```text
src/02_etl_vendas.py
```

O fluxo realizado é:

```text
raw_vendas
     ↓
Leitura dos dados
     ↓
Renomeação das colunas
     ↓
Conversão dos tipos
     ↓
Tratamento de data e hora
     ↓
Criação de novas colunas
     ↓
Validação dos dados
     ↓
Limpeza da tabela tratada
     ↓
Carga em vendas_tratadas
     ↓
Geração de vendas_tratadas.csv
```

---

## Transformações realizadas

As colunas originais foram renomeadas para facilitar a leitura e análise.

Exemplo:

```text
Invoice ID → id_venda
Branch → filial
City → cidade
Product line → linha_produto
Unit price → preco_unitario
Quantity → quantidade
Sales → valor_total
Payment → forma_pagamento
Rating → avaliacao
```

Também foram realizadas conversões de tipos:

- valores monetários para tipos numéricos;
- quantidade para inteiro;
- data para formato de data;
- horário para formato de hora.

---

## Colunas derivadas

Durante o ETL foram criadas novas informações a partir dos dados originais.

### Dia da semana

Obtido a partir da data da venda.

```text
dia_semana
```

### Mês da venda

```text
mes_venda
```

### Ano da venda

```text
ano_venda
```

### Valor sem imposto

Calculado por:

```text
valor_sem_imposto = valor_total - imposto
```

---

## Validações realizadas

Antes da carga na tabela tratada, foram realizadas verificações de qualidade dos dados.

### Valores nulos

Foi verificada a existência de valores nulos nas colunas.

Resultado:

```text
0 valores nulos
```

### Registros duplicados

Resultado:

```text
0 registros duplicados
```

### Identificadores duplicados

A coluna `id_venda` também foi validada.

Resultado:

```text
0 identificadores duplicados
```

### Validação financeira

Foi verificado se:

```text
valor_total - imposto = custo_mercadoria
```

Foi utilizado arredondamento de duas casas decimais para evitar diferenças causadas pela precisão de números do tipo `float`.

Resultado:

```text
0 divergências
```

---

## Reexecução do ETL

Antes de realizar uma nova carga, a tabela tratada é limpa utilizando:

```sql
TRUNCATE TABLE vendas_tratadas;
```

Depois os dados tratados são inseridos novamente.

Isso evita duplicação de registros caso o ETL seja executado mais de uma vez.

---

## Arquivo tratado

Após a execução do ETL, também é gerado o arquivo:

```text
data/processed/vendas_tratadas.csv
```

Esse arquivo contém os dados após todas as transformações e validações.

---

# Análise estatística

As análises foram realizadas no arquivo:

```text
src/03_estatistica.py
```

Foram utilizadas funções do Pandas como:

```python
sum()
mean()
min()
max()
count()
describe()
groupby()
value_counts()
```

---

## Principais indicadores

### Faturamento total

```text
322966.749
```

Aproximadamente:

```text
322.966,75
```

### Média das vendas

```text
322.966749
```

Aproximadamente:

```text
322,97
```

### Maior venda

```text
1042.65
```

### Menor venda

```text
10.6785
```

### Quantidade total de produtos vendidos

```text
5510
```

### Média das avaliações

```text
6.9727
```

### Total de vendas realizadas

```text
1000
```

---

## Faturamento por filial

O faturamento obtido por cada filial foi:

```text
Alex     106200.3705
Cairo    106197.6720
Giza     110568.7065
```

A filial com maior faturamento foi **Giza**.

Alex e Cairo apresentaram valores bastante próximos.

---

## Faturamento por linha de produto

```text
Electronic accessories    54337.5315
Fashion accessories       54305.8950
Food and beverages        56144.8440
Health and beauty         49193.7390
Home and lifestyle        53861.9130
Sports and travel         55122.8265
```

A linha com maior faturamento foi:

```text
Food and beverages
```

A linha com menor faturamento foi:

```text
Health and beauty
```

---

## Formas de pagamento

Quantidade de vendas por forma de pagamento:

```text
Ewallet        345
Cash           344
Credit card    311
```

A forma de pagamento mais utilizada foi **Ewallet**, seguida de muito perto por **Cash**.

---

## Avaliação média por linha de produto

Também foi analisada a avaliação média dos clientes para cada linha de produto.

A categoria com maior avaliação média foi:

```text
Food and beverages
```

com média aproximada de:

```text
7,11
```

---

## Faturamento por mês

Os dados analisados correspondem aos meses de janeiro, fevereiro e março de 2019.

```text
Janeiro      116291.868
Fevereiro     97219.374
Março        109455.507
```

O mês com maior faturamento foi **Janeiro**.

---

## Quantidade de vendas por mês

Também foi analisada a quantidade de transações realizadas em cada mês utilizando:

```python
count()
```

Essa análise permite comparar o número de vendas com o faturamento mensal.

---

## Ticket médio por mês

O ticket médio mensal foi calculado utilizando:

```python
mean()
```

sobre a coluna:

```text
valor_total
```

Isso permite identificar o valor médio gasto em cada transação de cada mês.

---

# Visualização dos dados

Os gráficos foram desenvolvidos no arquivo:

```text
src/04_graficos.py
```

Foi utilizada a biblioteca:

```text
Matplotlib
```

Os principais gráficos gerados foram:

### Faturamento por filial

Permite comparar visualmente o desempenho das filiais Alex, Cairo e Giza.

### Faturamento por linha de produto

Permite identificar quais categorias possuem maior participação no faturamento.

### Vendas por forma de pagamento

Apresenta a quantidade de transações realizadas utilizando:

- Ewallet;
- Cash;
- Credit card.

### Faturamento por mês

Apresenta a evolução do faturamento entre:

- Janeiro;
- Fevereiro;
- Março.

Os arquivos dos gráficos estão disponíveis em:

```text
graficos/
```

---

# Consultas SQL

As consultas desenvolvidas durante o projeto estão disponíveis em:

```text
sql/03_consultas.sql
```

Foram realizadas consultas para:

- quantidade total de registros;
- identificação das filiais;
- quantidade de vendas por filial;
- faturamento por filial;
- média de vendas por filial;
- menor e maior venda;
- cidades;
- linhas de produto;
- formas de pagamento;
- quantidade de transações por pagamento;
- faturamento por linha de produto;
- avaliação média por produto;
- identificação da maior venda;
- filtragem por período;
- identificação de valores nulos;
- identificação de registros duplicados;
- cálculo do valor médio das vendas.

---

# Como executar o projeto

## 1. Baixar o projeto

Clone o repositório ou faça o download dos arquivos.

Exemplo utilizando Git:

```bash
git clone URL_DO_REPOSITORIO
```

Depois entre na pasta do projeto:

```bash
cd Projeto_Supermarket_Sales
```

---

## 2. Instalar as dependências

As bibliotecas utilizadas estão registradas no arquivo:

```text
requirements.txt
```

Instale utilizando:

```bash
pip install -r requirements.txt
```

As principais bibliotecas utilizadas são:

```text
pandas
SQLAlchemy
psycopg2
python-dotenv
matplotlib
```

---

## 3. Configurar o PostgreSQL

É necessário possuir o PostgreSQL instalado e em execução.

Primeiro execute:

```text
sql/01_criar_banco.sql
```

Esse script cria:

```text
supermarket_sales_db
```

Depois conecte-se ao banco `supermarket_sales_db` e execute:

```text
sql/02_criar_tabelas.sql
```

Esse arquivo cria as tabelas:

```text
raw_vendas
vendas_tratadas
```

---

## 4. Importar os dados originais

O arquivo original está disponível em:

```text
data/raw/SuperMarket Analysis.csv
```

Os dados devem ser importados para a tabela:

```text
raw_vendas
```

No desenvolvimento deste projeto, a importação foi realizada utilizando o recurso de importação de dados do **DBeaver**.

Após a importação, pode-se validar a quantidade de registros utilizando:

```sql
SELECT COUNT(*)
FROM raw_vendas;
```

O resultado esperado é:

```text
1000
```

---

## 5. Configurar o arquivo .env

As informações de acesso ao banco de dados não são armazenadas diretamente no código Python.

Crie um arquivo chamado:

```text
.env
```

na raiz do projeto.

Utilize como referência o arquivo:

```text
.env.example
```

O `.env` deve possuir a seguinte estrutura:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=supermarket_sales_db
DB_USER=postgres
DB_PASSWORD=sua_senha
```

Substitua:

```text
sua_senha
```

pela senha utilizada no PostgreSQL.

O arquivo `.env` não deve ser enviado para o GitHub, pois contém informações privadas de conexão.

Por esse motivo ele está incluído no:

```text
.gitignore
```

---

## 6. Executar a inspeção inicial

Execute:

```bash
python src/01_leitura_dados.py
```

Esse script realiza a inspeção inicial do dataset, verificando:

- estrutura;
- quantidade de registros;
- colunas;
- tipos;
- valores nulos;
- duplicidades;
- estatísticas gerais.

---

## 7. Executar o ETL

Execute:

```bash
python src/02_etl_vendas.py
```

Esse script:

- lê os dados da tabela `raw_vendas`;
- renomeia as colunas;
- converte os tipos;
- transforma datas e horários;
- cria novas colunas;
- realiza validações;
- limpa a tabela `vendas_tratadas`;
- carrega os dados tratados;
- gera `vendas_tratadas.csv`.

Após a execução, a tabela deve possuir:

```text
1000 registros
```

A validação pode ser realizada utilizando:

```sql
SELECT COUNT(*)
FROM vendas_tratadas;
```

---

## 8. Executar as análises estatísticas

Execute:

```bash
python src/03_estatistica.py
```

Esse script calcula os principais indicadores e agrupamentos do projeto.

---

## 9. Gerar os gráficos

Execute:

```bash
python src/04_graficos.py
```

Esse script gera as visualizações utilizadas na análise.

Os gráficos são armazenados em:

```text
graficos/
```

---

git 

# Ordem de execução

Resumidamente, após configurar o banco de dados:

```text
01_leitura_dados.py
        ↓
02_etl_vendas.py
        ↓
03_estatistica.py
        ↓
04_graficos.py
```

Ou pelo terminal:

```bash
python src/01_leitura_dados.py
python src/02_etl_vendas.py
python src/03_estatistica.py
python src/04_graficos.py
```

---

# Conclusão

A análise permitiu observar diferenças de desempenho entre filiais, linhas de produto, formas de pagamento e períodos.

Entre os principais resultados encontrados:

- foram analisadas **1000 vendas**;
- foram comercializados **5510 produtos**;
- o faturamento total foi de aproximadamente **322.966,75**;
- a filial **Giza** apresentou o maior faturamento;
- **Food and beverages** foi a linha de produto com maior faturamento;
- **Ewallet** foi a forma de pagamento mais utilizada;
- janeiro apresentou o maior faturamento entre os meses analisados;
- a avaliação média dos clientes foi de aproximadamente **6,97**.

O projeto demonstra um fluxo completo de análise de dados, partindo de dados brutos, passando pelo armazenamento e transformação, até a geração de indicadores e visualizações para apoio à análise.
