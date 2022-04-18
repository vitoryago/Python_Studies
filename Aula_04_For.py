#AULA 1 - FOR

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

for i in range(len(produtos)):
    print('{} unidades produzidas de {}' .format(producao[i], produtos[i]))

# AULA 2 - FOR EM LISTA

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
texto = 'vitor.yagocp@gmail.com'

for item in produtos:
    print(item)

for ch in texto:
    print(ch)

#AULA 3 - FOR E IF
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000
i = 0

for venda in vendas:
    if venda >= meta:
        i +=1

porcentagem = i/len(vendas)
print('{:.2%}' .format(porcentagem))

#AULA 4 - ENUMERATE: FOR COM ITEM E INDICE

funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']

for i, item in enumerate(funcionarios):
    print('{} é o funcionário {}' .format(i, item))


estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
nivel_minimo = 50

for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print(produtos[i])
        print('{} está abaixo do nível mínimo, temos apenas {} unidades.' .format(produtos[i], estoque[i]))

#AULA 5 - EXERCÍCIOS
qtde = int(input('Quantas pessoas têm no quarto? '))
quarto = []

for i in range(qtde):
    nome = input('Qual o nome dela? ')
    cpf = input('Qual o CPF? ')
    hospede = [nome, 'cpf: {}' .format(cpf)]
    quarto.append(hospede)

print(quarto)

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

for item in vendas:
    if item[1] >= meta:
        print('Vendedor {} bateu a meta e fez R${:,.2f} de vendas.' .format(item[0], item[1]))
    else:
        print('Vendedor {} não bateu a meta, ele fez apenas R${:,.2f} de vendas' .format(item[0], item[1]))


produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

for i, produto in enumerate(produtos):
    if vendas2019[i] < vendas2020[i]:
        print('O produto {} vendeu {} unidades a mais em 2020 do que em 2019, o que representa acréscimo de {:.2%}' .format(produto, vendas2020[i]-vendas2019[i], vendas2019[i]/vendas2020[i]))

#AULA 6 - FOR DENTRO DE FOR 

estoque = [
    [294, 125, 269, 208, 783, 852, 259, 371, 47, 102, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453],
    [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549],
    [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522],
    [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362],
    [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 654],
]
fabricas = ['Lira Manufacturing', 'Fábrica Hashtag', 'Python Manufaturas', 'Produções e Cia', 'Manufatura e Cia']
nivel_minimo = 50
fabrica_baixo = []
for i, lista in enumerate(estoque):
    for qtde in lista:
        if qtde < nivel_minimo:
            if fabricas[i] in fabrica_baixo:
                pass
            else:
                fabrica_baixo.append(fabricas[i])
            
print(fabrica_baixo)

#AULA 7 - EXERCICIOS

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
acima_meta = []
melhor_vendedor = ''
maior_venda = 0
for venda in vendas:
    if venda[1] > meta:
        acima_meta.append(venda)
        if venda[1] > maior_venda:
            maior_venda = venda[1]
            melhor_vendedor = venda[0]


# print(acima_meta)
# print('{} dos vendedores bateram a meta' .format(len(acima_meta) / len(vendas)))
print(maior_venda)
print(melhor_vendedor)
