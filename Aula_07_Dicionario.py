#AULA 1 - DICIONARIOS

from functools import total_ordering


mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

qtde_iphone = vendas_tecnologia['ps5']
print(qtde_iphone)

# AULA 2 - VERIFICAR ITEM DICIONARIO

print(mais_vendidos['livros'])
print(mais_vendidos['lazer'])

print(vendas_tecnologia.get('notebook asus'))

if 'copo' in vendas_tecnologia:
    print(vendas_tecnologia['copo'])
else:
    print('Não está na variável')

if vendas_tecnologia.get('copo') == None:
    print('Copo não está na variável')

#AULA 3 - ADICIONAR, MODIFICAR E REMOVER ITENS DO DICIONÁRIO

lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}
print(lucro_1tri)
lucro_1tri['abril'] = 88000
print(lucro_1tri)

lucro_1tri.update(lucro_2tri)
print(lucro_1tri)

lucro_1tri['fevereiro'] = 88000
print(lucro_1tri)
lucro_1tri.update({'fevereiro': 150000})
print(lucro_1tri)

del lucro_1tri['abril']
print(lucro_1tri)

lucro_jun = lucro_1tri.pop('junho')
print(lucro_jun)
print(lucro_1tri)


lucro_1tri.clear()
print(lucro_1tri)

#AULA 4 - LOOP NO DICIONÁRIO

for chave in vendas_tecnologia:
    print('{}: {} unidades' .format(chave, vendas_tecnologia[chave]))

total_notebooks = 0
for chave in vendas_tecnologia:
    if 'notebook' in chave:
        total_notebooks += vendas_tecnologia[chave]

print(total_notebooks)

#AULA 5 - EXERCÍCIOS

niveis_co2 = {
    'AC': [325,405,429,486,402],
    'AL': [492,495,310,407,388],
    'AP': [507,503,368,338,400],
    'AM': [429,456,352,377,363],
    'BA': [321,508,372,490,412],
    'CE': [424,328,425,516,480],
    'ES': [449,506,461,337,336],
    'GO': [425,460,385,485,460],
    'MA': [361,310,344,425,490],
    'MT': [358,402,425,386,379],
    'MS': [324,357,441,405,427],
    'MG': [345,367,391,427,516],
    'PA': [479,514,392,493,329],
    'PB': [418,499,317,302,476],
    'PR': [420,508,419,396,327],
    'PE': [404,444,495,320,343],
    'PI': [513,513,304,377,475],
    'RJ': [502,481,492,502,506],
    'RN': [446,437,519,356,317],
    'RS': [427,518,459,317,321],
    'RO': [517,466,512,326,458],
    'RR': [466,495,469,495,310],
    'SC': [495,436,382,483,479],
    'SP': [495,407,362,389,317],
    'SE': [508,351,334,389,418],
    'TO': [339,490,304,488,419],
    'DF': [376,516,320,310,518], 
}

for estado in niveis_co2:
    media = sum(niveis_co2[estado])/len(niveis_co2[estado])
    if media > 450:
        print('{} está com níveis altíssimos de CO2 ({}), chamar uma equipe especializada para verificar a região' .format(estado, media))


video = {'uri': '/videos/465407533', 'name': '15 Atalhos no Excel para Ficar Mais Produtivo', 'download': [{'quality': 'source', 'type': 'source', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064518513?s=465407533_1602043255_5f2f93dd00b66eba66d481f913383b4f&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivosource.mp4', 'created_time': '2020-10-06T14:26:17+00:00', 'fps': 30, 'size': 402678442, 'md5': 'af09508ceceed4994554f04e8b931e22', 'public_name': 'Original', 'size_short': '384.02MB'}, {'quality': 'hd', 'type': 'video/mp4', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523157?s=465407533_1602043255_ab7b8353c59b5048032396ec5d95a276&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo175.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 173556205, 'md5': '3c05e1e69bd6b13eb1464451033907d2', 'public_name': 'HD 1080p', 'size_short': '165.52MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 960, 'height': 540, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523153?s=465407533_1602043255_f5ac38009ec5c0a13b30600c631446a3&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo165.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 89881848, 'md5': '4a5c5c96cdf18202ed20ca534fd88007', 'public_name': 'SD 540p', 'size_short': '85.72MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 426, 'height': 240, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522788?s=465407533_1602043255_16c69872e2c4e92cc949d0b772242959&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo139.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 27401450, 'md5': '91cc0229087ec94bf67f64b01ad8768d', 'public_name': 'SD 240p', 'size_short': '26.13MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 640, 'height': 360, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522787?s=465407533_1602043255_310b087e2fc8c5e1154ce7a33d10d60e&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo164.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 48627155, 'md5': '548640bf79ce1552a3401726bb0e4224', 'public_name': 'SD 360p', 'size_short': '46.37MB'}]}

for item in video:
    print(item)

print(video['download'][0]['link'])

#AULA 6 - MÉTODOS ÚTEIS DICIONÁRIOS

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

itens_dicionario = vendas_tecnologia.items()
print(itens_dicionario)

for item in vendas_tecnologia.items():
    print(item)

for produto, quantidade in vendas_tecnologia.items():
    print('{}: {} unidades' .format(produto, quantidade))

for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print('{}: {} unidades' .format(chave, vendas_tecnologia[chave]))

for produto, quantidade in vendas_tecnologia.items():
    if quantidade > 5000:
        print('{}: {} unidades' .format(produto, quantidade))

chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()
print(chaves)
print(valores)
chav = list(chaves)
print(list(chav))
print(list(valores))

for chave in vendas_tecnologia:
    print('{}: {} unidades' .format(chave, vendas_tecnologia[chave]))

print( '-' * 40)

lista_chaves = list(chaves)
lista_chaves.sort()

for chave in lista_chaves:
    print('{}: {} unidades' .format(chave, vendas_tecnologia[chave]))

#AULA 7 - TRANSFORMANDO LISTA EM DICIONARIO

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

lista_tuplas = zip(produtos, vendas)
# for item in lista_tuplas:
#     print(item)
dicionario = dict(lista_tuplas)
print(dicionario)