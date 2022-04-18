#AULA 1 - MAP
def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto

produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', ' BSA151', 'BEB23']

produtos = list(map(padronizar_texto, produtos))
print(produtos)

# AULA 2 - USANDO FUNCAO COMO PARAMETRO

produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
produtos.sort(key = str.casefold)
print(produtos)

vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}

def segundo_item(tupla):
    return[1]

lista_vendas =  list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item, reverse=True)
lista_vendas = dict(lista_vendas)
print(lista_vendas)

#AULA 3 - LAMBDA EXPRESSIONS

minha_funcao = lambda num: num * 2
print(minha_funcao(5))

preco_imposto = lambda preco: preco * (1.0 + 0.3)
print(preco_imposto(30))

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

preco_com_imposto = list(map(lambda preco: preco* 1.3, preco_tecnologia.values()))
print(preco_com_imposto)

produtos_acima2000 = dict(list(filter(lambda item: item[1] > 2000, preco_tecnologia.items())))

#AULA 4 - GERAR FUNÇÕES COM LAMBDA EXPRESSION

def calcular_imposto(imposto):
    return lambda preco: preco * imposto

calcular_preco_produto = calcular_imposto(0.1)
calcular_preco_servico = calcular_imposto(0.15)
calcular_preco_royalties = calcular_imposto(0.20)

print(calcular_preco_produto(100))
print(calcular_preco_servico(100))
print(calcular_preco_royalties(100))