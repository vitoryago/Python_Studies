from numpy import product
import pandas as pd
import matplotlib.pyplot as plt
import requests
import io

vendas_df = pd.read_csv(r'C:\Users\Vitor Yago\Documents\Python\Contoso - Vendas  - 2017.csv', sep=';')
#AULA 1 - IMPORTANDO CSV DE SITES
# url = 'https://drive.google.com/uc?authuser=0&id=1UzlPy6CZQeAzDXhfc_2sHEyK_Jb50vJs&export=download'
# cotacao_df = pd.read_csv(url)
# print(cotacao_df)

# url = 'http://portalweb.cooxupe.com.br:8080/portal/precohistoricocafe_2.jsp;jsessionid=87A1B21EF6E41ED0033AC0278882F1D2?d-3496238-e=2&6578706f7274=1'
# conteudo_url = requests.get(url).content
# arquivo = io.StringIO(conteudo_url.decode('latin1'))
# cafe_df = pd.read_csv(arquivo, sep=r'\t', engine='python')
# print(cafe_df)

#AULA 2 - BARRA DE PROGRESSO PYTHON

# from tqdm import tqdm

# pbar = tqdm(total=len(vendas_df['ID Loja']), position=0, leave=True)

# for i,id_loja in enumerate(vendas_df['ID Loja']):
#     pbar.update()
#     if id_loja == 222:
#         vendas_df.loc[i, 'Quantidade Devolvida'] += 1

# print(vendas_df)

#AULA 3 - MINI PROJETO DE ANÁLISE DE DADOS

