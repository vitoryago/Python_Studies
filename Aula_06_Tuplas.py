#AULA 1 - TUPLAS

vendas = ('Vitor', '25/08/2020', '14/10/1996', 2000, 'Estagiário')

nome = vendas[0]
contrato = vendas[1]
nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print(vendas[0])

nome, contrato, nascimento, salario, cargo = vendas
print(nome)

#AULA 2 - LISTA DE TUPLAS - LOOP COM TUPLAS

vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 7500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 7017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

faturamento = 0

for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += unidades * valor_unitario

print(faturamento)

mais_vendido = 0
product = ''

for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if data == '21/08/2020':
        if mais_vendido < unidades:
            mais_vendido = unidades
            product = produto
        else:
            continue

print(mais_vendido)
print(produto)

meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

for vendedor, qtde in vendas:
    if qtde > meta:
        print('{} bateu a meta, vendeu {} unidades' .format(vendedor, qtde))

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

for produto, vendas2019, vendas2020 in vendas_produtos:
    if vendas2019 < vendas2020:
        print('{} teve {} vendas em 2019, {} vendas em 2020. Crescimento de {:.1%}' .format(produto, vendas2019, vendas2020, (vendas2020/vendas2019)-1))