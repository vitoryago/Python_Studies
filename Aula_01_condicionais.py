#AULA 1: CONDICIONAIS IF, IDENTAÇÃO E COMO FUNCIONA IF DENTRO DE IF

meta = 50000
qtde_vendas = 150000
rendimento = 0.5
preco = 1500
custo = qtde_vendas*rendimento*preco
faturamento = qtde_vendas*preco

if(qtde_vendas > 5*meta) | (rendimento < 0.7):
    print('A meta foi batida, quantidade vendida {} {}' .format(qtde_vendas, meta))
    if(qtde_vendas < 100000):
        print('A quantidade vendida foi {}, logo, nao chegamos no valor de 100.000' .format(qtde_vendas))
    else:
        print('Alem da meta ser batida, conseguimos bater o record de 100.000 vendidos')
else:
    print('Nao batemos a meta')

#AULA 2: ELIF

meta = 20000
vendas = 10000

if vendas > 3*meta:
    print('Bateu record')
elif vendas > 2*meta:
    print('Dobrou a meta {}' .format(2*meta))
elif vendas > 1.5*meta:
    print('Superou a meta em 50% mas nao dobrou')
elif vendas > meta:
    print('Bateu a meta')
else:
    print('Nao bateu a meta')

#AULA 3: COMPARADORES

faturamento1 = 1500
faturamento2 = 1500
email = 'vitor.yagocpgmail.com'

if faturamento1 == faturamento1:
    print('Faturamentos iguais')
else:
    print('Faturamentos diferentes')

if not '@' in email:
    print('Email invalido')

else:
    print('Email valido')

#AULA 4: EXERCÍCIOS

vendas_funcionario1 = int(input('Qual foi as vendas do funcionario 1?'))
vendas_funcionario2 = int(input('Qual foi as vendas do funcionario 2?'))
vendas_funcionario3 = int(input('Qual foi as vendas do funcionario 3?'))

if vendas_funcionario1 >= 1000 or vendas_funcionario3 >= 5000:
    if vendas_funcionario1 >= 2000:
        print('O funcionario 1 ganhou {} de bonus.' .format(0.15*vendas_funcionario1))
    else:
        print('O funcionario 1 ganhou {} de bonus. E o funcionario 3 ficou rico' .format(0.1*vendas_funcionario1))
else:
    print('O funcionario 1 nao ganhou bonus.')

if vendas_funcionario2 >= 1000:
    if vendas_funcionario2 >= 2000:
        print('O funcionario 2 ganhou {} de bonus.' .format(0.15*vendas_funcionario2))
    else:
        print('O funcionario 2 ganhou {} de bonus.' .format(0.1*vendas_funcionario2))
else:
    print('O funcionario 2 nao ganhou bonus.')

if vendas_funcionario3 >= 1000:
    if vendas_funcionario3 >= 2000:
        print('O funcionario 3 ganhou {} de bonus.' .format(0.15*vendas_funcionario3))
    else:
        print('O funcionario 3 ganhou {} de bonus.' .format(0.1*vendas_funcionario3))
else:
    print('O funcionario 3 nao ganhou bonus.')

nome_produto = input('Digite o nome do produto:')
categoria = input('Digite a categoria do produto:')
quantidade = int(input('Digite a quantidade em estoque:'))

if categoria and nome_produto and quantidade:
    if categoria == 'alimentos' and quantidade <= 50:
        print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque.' .format(nome_produto, quantidade))

    elif categoria == 'bebidas' and quantidade <= 75:
        print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque.' .format(nome_produto, quantidade))

    elif categoria == 'limpeza' and quantidade <= 30:
        print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque.' .format(nome_produto, quantidade))
else:
    print('Preencha corretamente.')