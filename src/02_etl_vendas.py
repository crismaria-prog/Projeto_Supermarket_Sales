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

df_vendas = df_vendas.rename(columns={
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