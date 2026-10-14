import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carrega as variáveis do arquivo .env
load_dotenv()

# Busca as configurações do banco no .env
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

#Conferência temporária
print("HOST:", host)
print("PORT:", port)
print("DATABASE:", database)
print("USER:", user)
print("PASSWORD carregada:", password is not None)


# Cria a conexão com o PostgreSQL
engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
)

print("Conexão com o banco de dados estabelecida com sucesso!")

df_vendas = pd.read_sql(
    "SELECT * FROM raw_vendas",
    engine
)

print(df_vendas.head())
print(df_vendas.shape)




# existe 1000 registros no banco de dados e 18 colunass 

df_vendas = df_vendas.rename(columns={ # renomeando as colunas para português, para melhor entendimento e análise
    "Invoice ID": "id_venda",
    "Branch": "filial",
    "City": "cidade",
    "Customer type": "tipo_cliente",
    "Gender": "genero",
    "Product line": "linha_produto",
    "Unit price": "preco_unitario",
    "Quantity": "quantidade",
    "Tax 5%": "imposto",
    "Sales": "valor_total",
    "Date": "data_venda",
    "Time": "hora_venda",
    "Payment": "forma_pagamento",
    "cogs": "custo_mercadoria",
    "gross margin percentage": "margem_percentual",
    "gross income": "receita_bruta",
    "Rating": "avaliacao"
})

print(df_vendas.columns)

colunas_numericas = [
    "preco_unitario",
    "imposto",
    "valor_total",
    "custo_mercadoria",
    "margem_percentual",
    "receita_bruta",
    "avaliacao"
]

for coluna in colunas_numericas:
    df_vendas[coluna] = pd.to_numeric(df_vendas[coluna])
    print(f"Coluna {coluna} convertida para numérica.")

df_vendas["quantidade"] = pd.to_numeric(
    df_vendas["quantidade"]
).astype(int)
print(df_vendas.dtypes)

df_vendas["data_venda"] = pd.to_datetime(
    df_vendas["data_venda"],
    format="%m/%d/%Y"
)

df_vendas["hora_venda"] = pd.to_datetime(
    df_vendas["hora_venda"],
    format="%I:%M:%S %p"
).dt.time

print(df_vendas[["data_venda", "hora_venda"]].head())
print(df_vendas.dtypes)

df_vendas["dia_semana"] = df_vendas["data_venda"].dt.day_name()
df_vendas["mes_venda"] = df_vendas["data_venda"].dt.month
df_vendas["ano_venda"] = df_vendas["data_venda"].dt.year
df_vendas["valor_sem_imposto"] = (
    df_vendas["valor_total"] - df_vendas["imposto"]
)

print(
    df_vendas[
        [
            "data_venda",
            "dia_semana",
            "mes_venda",
            "ano_venda",
            "valor_total",
            "imposto",
            "valor_sem_imposto"
        ]
    ].head()
)

print(df_vendas.isna().sum())

print(df_vendas.duplicated().sum())

print(df_vendas["id_venda"].duplicated().sum())

diferencas = (
    df_vendas["valor_sem_imposto"].round(2) ## Validação financeira com arredondamento de 2 casas decimais para evitar diferenças de precisão do tipo float
    != df_vendas["custo_mercadoria"].round(2)
).sum()

print(diferencas)

df_vendas = df_vendas.drop(columns=["id_ingestao"]) # removendo id_ingestao, pois não é necessário para análises futuras


colunas_finais = [    #ordenando as colunas para melhor visualização e análise
    "id_venda",
    "filial",
    "cidade",
    "tipo_cliente",
    "genero",
    "linha_produto",
    "preco_unitario",
    "quantidade",
    "imposto",
    "valor_total",
    "data_venda",
    "hora_venda",
    "forma_pagamento",
    "custo_mercadoria",
    "margem_percentual",
    "receita_bruta",
    "avaliacao",
    "dia_semana",
    "mes_venda",
    "ano_venda",
    "valor_sem_imposto"
]

df_vendas = df_vendas[colunas_finais]

print(df_vendas.columns)
print(df_vendas.shape)

with engine.begin() as conexao: # para poder rodar o codigo mais de uma vez sem criar duplicidade de dados, é necessário truncar a tabela antes de inserir os novos dados
    conexao.exec_driver_sql("TRUNCATE TABLE vendas_tratadas;")

df_vendas.to_sql(
    "vendas_tratadas", #tabela de destino no banco de dados
    engine, # conexão com PostgreSQL
    if_exists="append", #para adicionar os dados à tabela existente, sem sobrescrever
    index=False # não envia o indice do pandas como uam coluna extra 

)
print("Dados carregados com sucesso na tabela vendas_tratadas do banco de dados PostgreSQL!")


df_vendas.to_csv(
    "data/processed/vendas_tratadas.csv",
    index=False
)

print("Arquivo vendas_tratadas.csv salvo com sucesso!")