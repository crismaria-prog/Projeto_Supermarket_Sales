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




