import os
import pandas as pd
import matplotlib.pyplot as plt # Criação de grasficos utilizando a biblioteca matplotlib
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carregando variáveis de ambiente do arquivo .env

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
)

df_vendas = pd.read_sql(
    "SELECT * FROM vendas_tratadas",
    engine
)

# Grafico de faturamento por filial

vendas_por_filial = df_vendas.groupby("filial")["valor_total"].sum()

vendas_por_filial.plot(kind="bar")

plt.title("Faturamento por filial")
plt.xlabel("Filial")
plt.ylabel("Faturamento")

plt.show()


# Grafico de faturamento por linha de produto

faturamento_por_produto = df_vendas.groupby("linha_produto")["valor_total"].sum()

faturamento_por_produto.plot(kind="bar", color="orange")

plt.title("Faturamento por linha de produto")
plt.xlabel("Linha de produto")
plt.ylabel("Faturamento")

plt.xticks(rotation=35, ha="right")
plt.tight_layout()

plt.show()

# Grafico de vendas por forma de pagamento

pagamentos = df_vendas["forma_pagamento"].value_counts()

pagamentos.plot(
    kind="bar",
    color="green"
)

plt.title("Quantidade de vendas por forma de pagamento")
plt.xlabel("Forma de pagamento")
plt.ylabel("Quantidade de vendas")

plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

df_vendas["mes_nome"] = df_vendas["mes_venda"].replace({
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março"
})



# Grafico de faturamento por mês

faturamento_por_mes = df_vendas.groupby("mes_venda")["valor_total"].sum()

faturamento_por_mes.index = [
    "Janeiro",
    "Fevereiro",
    "Março"
]
faturamento_por_mes.plot(
    kind="bar",
    color="purple"
)

plt.title("Faturamento por mês")
plt.xlabel("Mês")
plt.ylabel("Faturamento")

plt.xticks(rotation=0)
plt.tight_layout()

plt.show()