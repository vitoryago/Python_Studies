#AULA 1 - LENDO ARQUIVO CSV

import pandas as pd

# dataframe = pd.read_csv('Contoso - Vendas - 2017.csv', sep = ';')
dataframe = pd.read_csv(r'C:\Users\Vitor Yago\Documents\Python\Contoso - Vendas - 2017.csv', sep = ';')
print(dataframe)