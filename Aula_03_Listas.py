#AULA 1: LISTAS

from audioop import reverse
from functools import total_ordering
from math import prod
from ntpath import join
from re import I
from numpy import sort


produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet', 'monitor']
vendas = [6000, 2000, 3000, 4000, 5000, 1000]
print(produtos[0])
i = produtos.index('celular')
estoque = vendas[i]
print('A quantidade em estoque do {} é de {}' .format(produtos[i], vendas[i]))

produto = input('Digite o nome do produto: ')
if produto in produtos:
    i = produtos.index(produto)
    print('O estoque do produto digitado ({}) é de {}' .format(produtos[i],vendas[i]))
else:
    print('Produto não encontrado')
produtos.append('iPad')
print(produtos)
removido = produtos.pop(2)
produtos.remove('tv')
print(produtos)
print('Removemos o {} da lista' .format(removido))
print(vendas.index(max(vendas)))
produtos.extend(vendas)
todos = produtos + vendas
produtos.sort()
vendas.sort(reverse=True)
print(produtos)
print(vendas)
print('\n' .join(produtos))
prod = 'apple, samsung, motorola'
lista = prod.split(', ')
print(lista)

#AULA 2 - EXERCÍCIOS LISTA

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_total = vendas_1sem + vendas_2sem
i_max = vendas_total.index(max(vendas_total))
i_min = vendas_total.index(min(vendas_total))

print('O mês que mais vendeu no ano foi o mês de {} com um valor total de R${:,.2f}. E o mês que menos vendeu foi o mês de {} com um valor total de R${:,.2f}.' .format(meses[i_max], max(vendas_total), meses[i_min], min(vendas_total)))
top_3 = []
tot = vendas_total
tot.sort(reverse=True)
print(tot)
top_3.append(tot[0])
top_3.append(tot[1])
top_3.append(tot[2])
print(top_3)

#AULA 3 - ALTERAÇÕES INCREMENTAIS
lista = ['mac', 'iphone']
vendas = [100, 200]
lista2 = lista.copy()
lista3 = lista[:]
vendas = vendas + [500]
lista = lista + ['Ipad']
soma_vendas = 800

print(lista)
print(lista2)
print(lista3)

email = 'Esse mês vendemos um total de {} produtos, sendo: \n{} unidades de {}\n{} unidades de {}' .format(soma_vendas, vendas[0], lista[0], vendas[1], lista[1])
#print(email)

email = email + '\n{} unidades de {}' .format(vendas[2], lista[2])

print(email)

#AULA 4 - LISTA DE LISTAS

vendedores = ['Lira', 'Vitor', 'Brenda', 'Diego']
produtos = ['IPad', 'iPhone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]

vendas_ipad_Lira = vendas[0][0]
# print(vendas_ipad_Lira)

vendas_iphone_diego = vendas[3][1]
# print(vendas_iphone_diego)

vendas_iphone_total = vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1]
# print(vendas_iphone_total)

vendas[0][1] = 50
# print(vendas)

vendas_mac = [10, 15, 6, 70]

vendas[0].append(vendas_mac[0])
vendas[1].append(vendas_mac[1])
vendas[2].append(vendas_mac[2])
vendas[3].append(vendas_mac[3])

print(vendas)

#AULA 5 - EXERCÍCIO

produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

if 'livro' in produtos:
    i = produtos.index('livro')
    total_antigo = produtos_ecommerce[i][0] * produtos_ecommerce[i][1]
    produtos_ecommerce[i][1] = produtos_ecommerce[i][1] * 1.1
    total_novo = produtos_ecommerce[i][0] * produtos_ecommerce[i][1]
    print('O valor total que pagavamos de imposto era R${:,.2f}, agora pagamos R${:,.2f}, resultando em um acréscimo de R${:,.2f}' .format(total_antigo, total_novo, total_novo - total_antigo))

    print(produtos_ecommerce[i][1])