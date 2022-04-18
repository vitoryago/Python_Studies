# AULA 1 - O QUE É

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']

for produto in produtos:
    print(produto)

texto = 'lira@gmail.com'

for ch in texto:
    print(ch)

produtos = ('iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus')

for produto in produtos:
    print(produto)

vendas_produtos = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

for produto in vendas_produtos:
    print(produto)
    print('{}: {} unidades'.format(produto, vendas_produtos[produto]))

#AULA 2 - RANGE

produtos = ['arroz', 'feijao', 'macarrao', 'atum', 'azeite']
estoque = [50, 100, 20, 5, 80]

for i in range(5):
    print('{}: {} unidades' .format(produtos[i], estoque[i]))

funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo']
vendas = [2750, 1900, 1500, 1200, 1111, 1100, 999, 900, 880, 870, 800, 800, 450, 400, 300, 300, 120, 90, 80, 70]

print('Funcionários Classe B: ')
for i in range(3, 18):
    print('{} fez {} vendas' .format(funcionarios[i], vendas[i]))

for i in range(0, 1000, 100):
    print(i)

#AULA 3 - SET

set_produtos = {'arroz', 'feijao', 'macarrao', 'atum', 'azeite'}

print(set_produtos)

cpf_clientes = ['762.196.080-97', '263.027.380-67', '827.363.930-40', '925.413.640-91', '870.565.160-33', '892.080.930-50', '462.126.030-81', '393.462.330-10', '393.462.330-10', '393.462.330-10', '988.305.810-11', '596.125.830-05', '596.125.830-05', '990.236.770-48']

print(len(cpf_clientes))
set_cpf = set(cpf_clientes)
print(len(set_cpf))

cpf_clientes_unicos = list(set_cpf)
print(cpf_clientes_unicos)