import pandas as pd
df_vendas = pd.read_csv('Supermarket Analysis.csv')
print(df_vendas.columns)
print(df_vendas.head())
print(df_vendas.shape)
print(df_vendas.dtypes)

# Ao realizar o print do df_vendas.dtypes, pude observar que a coluna Date e Time, estão como string,
# Para realizar análises temporais, é importante converter essa coluna

df_vendas.info() # para verificar se há valores nulos e o tipo de dado de cada coluna

print(df_vendas.isna().sum()) # para confirmar a quantidade exata de valores nulos em cada coluna

# A verificação de valores nulos retornou 0 para todas as colunas. Portanto, não possui valores ausentes

print(df_vendas.duplicated().sum())
print(df_vendas['Invoice ID'].duplicated().sum())

# Não há valores duplicados no dataframe, nem na coluna invoice id. Portanto, não é necessário realizar a remoção de valores duplicados.

print(df_vendas.describe())
print(df_vendas['Date'].head())


datas_convertidas = pd.to_datetime(df_vendas['Date'], format='%m/%d/%Y')
print(datas_convertidas.min().strftime("%d/%m/%Y"))
print(datas_convertidas.max().strftime("%d/%m/%Y"))
