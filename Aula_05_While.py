#AULA 1 - WHILE

venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia: ')
vendas = []

while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia: ')


print('Registro Finalizado. As vendas cadastradas foram: {}'.format(vendas))

# AULA 2 - LOOP INFINITO

vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50

i = 0
print('oi')
while vendas[i] > meta:
    print('{} bateu a meta. Vendas: {}.' .format(vendedores[i], vendas[i]))

#AULA 3 - EXERCÍCIO WHILE

from numpy import append

vendas = []

while produto:
    produto = input('Qual o seu produto? ')
    if produto != '':
            quantidade = int(input('Qual a quantidade? '))
            vendas.append([produto, quantidade])

print(vendas)