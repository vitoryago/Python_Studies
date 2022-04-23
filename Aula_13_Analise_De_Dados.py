#AULA 1 - LENDO ARQUIVO CSV

from numpy import product
import pandas as pd
import matplotlib.pyplot as plt

# dataframe = pd.read_csv('Contoso - Vendas - 2017.csv', sep = ';')
# dataframe = pd.read_csv(r'C:\Users\Vitor Yago\Documents\Python\Contoso - Vendas  - 2017.csv', sep = ';')
# print(dataframe)

#AULA 2 - MULTIPLOS ARQUIVOS

vendas_df = pd.read_csv(r'C:\Users\Vitor Yago\Documents\Python\Contoso - Vendas  - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'C:\Users\Vitor Yago\Documents\Python\Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'C:\Users\Vitor Yago\Documents\Python\Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'C:\Users\Vitor Yago\Documents\Python\Contoso - Clientes.csv', sep=';')

# print(vendas_df)
# print(produtos_df)
# print(lojas_df)
# print(clientes_df)

# clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1)
# print(clientes_df)

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
# print(vendas_df)
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})
# print(vendas_df)

#AULA 3 - ANALISES - Qual o cliente que mais comprou?
# frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()
# email_clientes = ['karen33@adventure-works.com', 'chloe77@adventure-works.com', 'julia43@adventure-works.com', 'destiny66@adventure-works.com', 'gilbert9@adventure-works.com']
# print(type(frequencia_clientes))
# plt.plot(frequencia_clientes[:5])
# plt.show()
# plt.bar(email_clientes, frequencia_clientes[:5])
# plt.show()

#AULA 4 - ANALISES - QUAL LOJA MAIS VENDE?
vendas_lojas = vendas_df.groupby('Nome da Loja').sum()
vendas_lojas = vendas_lojas[['Quantidade Vendida']].sort_values('Quantidade Vendida', ascending=False)
# print(vendas_lojas)

maior_valor = vendas_lojas['Quantidade Vendida'].max()
melhor_loja = vendas_lojas['Quantidade Vendida'].idxmax()
# print(melhor_loja, maior_valor)

qtde_vendida = vendas_df['Quantidade Vendida'].sum()
qtde_devolvida = vendas_df['Quantidade Devolvida'].sum()

# print('{:.2%} ' .format(qtde_devolvida/qtde_vendida))

# lojax = vendas_df[vendas_df['ID Loja'] == 306]
# qtde_vendida = lojax['Quantidade Vendida'].sum()
# qtde_devolvida = lojax['Quantidade Devolvida'].sum()
# print('{:.2%} ' .format(qtde_devolvida/qtde_vendida))

df_loja306_semdev = vendas_df[(vendas_df['ID Loja'] == 306) & (vendas_df['Quantidade Devolvida'] == 0)]
# print(df_loja306_semdev)

vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'], format = '%d/%m/%Y')
vendas_df['Ano da Venda'] = vendas_df['Data da Venda'].dt.year
# print(vendas_df)

#AULA 5 - LOC E ILOC
# novo_produtos_df = pd.read_csv(r'C:\Users\Vitor Yago\Documents\Python\Contoso - Cadastro Produtos.csv', sep=';')

# novo_produtos_df = novo_produtos_df.set_index('Nome do Produto')
# print(novo_produtos_df.loc['Contoso Wireless Laser Mouse E50 Grey', 'Preco Unitario'])

# print(novo_produtos_df.iloc[2,5])

#AULA 6 - CONVERTER PROGRAMA EM CSV

# vendas_df.to_csv('Novo Vendas 2017.csv', sep = ';')

# vendas_produtos = {'iphone': [558147, 951642], 'galaxy': [712350, 244295], 'ipad': [573823, 26964], 'tv': [405252, 787604], 'máquina de café': [718654, 867660], 'kindle': [531580, 78830], 'geladeira': [973139, 710331], 'adega': [892292, 646016], 'notebook dell': [422760, 694913], 'notebook hp': [154753, 539704], 'notebook asus': [887061, 324831], 'microsoft surface': [438508, 667179], 'webcam': [237467, 295633], 'caixa de som': [489705, 725316], 'microfone': [328311, 644622], 'câmera canon': [591120, 994303]}

# vendas_produtos_df = pd.DataFrame.from_dict(vendas_produtos)
# vendas_produtos_df = pd.DataFrame.from_dict(vendas_produtos, orient = 'index')
# vendas_produtos_df = vendas_produtos_df.rename(columns={0: 'Vendas 2019', 1: 'Vendas 2020'})
# print(vendas_produtos_df)

# vendas_produtos_df.to_csv(r'Nova Venda.csv', sep=';', encoding='latin1')
