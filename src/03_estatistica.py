import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

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

print(df_vendas.head())
print(df_vendas.shape)
print(df_vendas.describe())

faturamento_total = df_vendas["valor_total"].sum() # soma de todo o faturamento de quanto vendeu no total
media_vendas = df_vendas["valor_total"].mean() # média das vendas para saber qnto vale uma venda em média
maior_venda = df_vendas["valor_total"].max() # encontra o maior valor de venda, para saber qual foi a maior venda
menor_venda = df_vendas["valor_total"].min() # Encotra o menor valor de venda, para saber qual foi a menor venda

print("\nFaturamento total:", faturamento_total)
print("\nMédia das vendas:", media_vendas)
print("\nMaior venda:", maior_venda)
print("\nMenor venda:", menor_venda)

quantidade_total = df_vendas["quantidade"].sum() # soma da quantidade de produtos vendi
media_avaliacao = df_vendas["avaliacao"].mean() # média das avaliações dos clientes, para saber se estão satisfeitos com o atendimento e produtos
total_vendas = df_vendas["id_venda"].count() # quantas vendas foram realizadas no total 

print("\nQuantidade total de produtos vendidos:", quantidade_total)
print("\nMédia das avaliações:", media_avaliacao)
print("\nTotal de vendas realizadas:", total_vendas)

vendas_por_filial = df_vendas.groupby("filial")["valor_total"].sum() # agrupa as vendas por filial e soma o valor total de vendas de cada filial
print("\nVendas por filial:")
print(vendas_por_filial)

vendas_por_produto = df_vendas.groupby("linha_produto")["valor_total"].sum() # agrupa as vendas por produto e soma o valor total de vendas de cada produto
print("\nVendas por produto:")
print(vendas_por_produto)

vendas_por_pagamento = df_vendas["forma_pagamento"].value_counts() # conta a quantidade de vendas por forma de pagamento
print("\nVendas por forma de pagamento:")
print(vendas_por_pagamento)

# A filial da Giza teve o maior faturamento, com um total de vendas de R$ 110568.7065 
# A filial do Cairo teve o segundo maior faturamento, com um total de vendas de R$ 106197.6720
# A filial do Alex teve o menor faturamento, com um total de vendas de R$ 106200.3705

# O metodo mais utilizado foi Ewallet por 345 vendas, já o metodo cash foi utilizado em 344 vendas e credit card foi 311 vendas



avaliacao_por_produto = df_vendas.groupby("linha_produto")["avaliacao"].mean() # Qual categoria de produto recebeu e média de avaliação mais alta dos clientes

print(avaliacao_por_produto)

faturamento_por_mes = df_vendas.groupby("mes_venda")["valor_total"].sum()

print(faturamento_por_mes)

df_vendas["mes_nome"] = df_vendas["mes_venda"].replace({
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março"
})

faturamento_por_mes = df_vendas.groupby("mes_nome")["valor_total"].sum() # faturamento por mês 

print("\nFaturamento por mês:")
print(faturamento_por_mes)

vendas_por_mes = df_vendas.groupby("mes_nome")["id_venda"].count() # Quantas vendas ocorreram por mês

print("\nVendas por mês:")
print(vendas_por_mes) 

ticket_medio_por_mes = df_vendas.groupby("mes_nome")["valor_total"].mean() # Para saber o ticket médio mensal

print("\nTicket médio por mês:")
print(ticket_medio_por_mes)
