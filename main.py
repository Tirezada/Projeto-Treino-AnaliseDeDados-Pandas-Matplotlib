import pandas as pd
import matplotlib.pyplot as plt

df_vendas = pd.read_excel('vendas_ficticias.xlsx')
#print(df_vendas.head())

print('\n--- Análise de Quantidades Totais ---')
qnt_categoria = df_vendas.groupby('Categoria')['Quantidade'].sum().sort_values(ascending=False)
qnt_cidade = df_vendas.groupby('Cidade')['Quantidade'].sum().sort_values(ascending=False)
qnt_produtos = df_vendas.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
print('\n', qnt_categoria.to_string())
print('\n', qnt_cidade.to_string())
print('\n', qnt_produtos.to_string())

print('\n--- Análise de Vendas Totais ---')
vendas_categoria = df_vendas.groupby('Categoria')['Valor_Total'].sum().sort_values(ascending=False) 
vendas_cidade = df_vendas.groupby('Cidade')['Valor_Total'].sum().sort_values(ascending=False) 
vendas_produtos = df_vendas.groupby('Produto')['Valor_Total'].sum().sort_values(ascending=False) 
print('\n', vendas_categoria.to_string())
print('\n', vendas_cidade.to_string())
print('\n', vendas_produtos.to_string())

print('\n--- Quantidade Totais de Vendas ---')
qnt_total = df_vendas['Quantidade'].sum()
print(f'Quantidade total de vendas: {qnt_total}')

print('\n--- Categoria Mais Lucrativa ---')
print(f'Categoria mais lucrativa: {vendas_categoria.index[0]}, R$ {vendas_categoria.iloc[0]:.2f} ')

print('\n--- Produto Mais Lucrativo ---')
print(f'Produto mais lucrativo: {vendas_produtos.index[0]}, R$ {vendas_produtos.iloc[0]:.2f} ')

print('\n--- Ticket Médio ---')
ticket_medio = df_vendas['Valor_Total'].sum() / df_vendas['Quantidade'].sum()
print(f'Ticket médio: R$ {ticket_medio:.2f}')

print('\n--- Cidade Mais Lucrativa ---')
print(f'Cidade mais lucrativa: {vendas_cidade.index[0]}, R$ {vendas_cidade.iloc[0]:.2f} ')

df_vendas['Data'] =  pd.to_datetime(df_vendas['Data'])
df_vendas['Mês'] =  df_vendas['Data'].dt.month

vendas_mes = df_vendas.groupby('Mês')['Quantidade'].sum().sort_values(ascending=False)
lucro_mes = df_vendas.groupby('Mês')['Valor_Total'].sum().sort_values(ascending=False)
print('\n--- Vendas por Mês(Qntd) ---')
print(vendas_mes.to_string())

print('\n--- Vendas por Mês(R$) ---')
print(lucro_mes.to_string())

print('\n--- Mês mais Lucrativo ---')
print(f'Mês mais lucrativo: {lucro_mes.index[0]}, R$ {lucro_mes.iloc[0]:.2f} ')

vendas_categoria.plot(kind='bar')

plt.title('Faturamento por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor Total')

plt.show()

vendas_cidade.plot(kind='line')

plt.title('Faturamento por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Valor Total')

plt.show()

vendas_produtos.plot(kind='pie')

plt.title('Faturamento por Produtos')
plt.xlabel('Produtos')
plt.ylabel('Valor Total')

plt.show()
