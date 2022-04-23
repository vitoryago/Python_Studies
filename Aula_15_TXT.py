#EXERCICIO 1 - ESCREVENDO SEM USAR O WITH

# #AULA 1 - EXERCICIO COM ARQUIVO TXT
# arquivo = open('Alunos.txt', 'r')

# linhas = arquivo.readlines()

# #Deletando as 4 primeiras linhas pois não fazem parte da analise
# del linhas[:4]

# #Criar indicadores
# qtde_anuncio = 0
# qtde_yt_org = 0
# qtde_org = 0
# qtde_igfb_org = 0
# qtde_site_org = 0

# #Percorrendo arquivo e contando quantidade de cada iteração
# for linha in linhas:
#     email, origem = linha.split(',')
#     if '_org' in origem:
#         qtde_org += 1
#         if 'hashtag_yt_org' in origem:
#             qtde_yt_org += 1
#         if 'hashtag_site_org' in origem:
#             qtde_site_org += 1
#         if ('hashtag_igfb_org' in origem) or ('hashtag_ig_org' in origem):
#             qtde_igfb_org += 1
#     else:
#         qtde_anuncio +=1


# print('Quantidade Anuncio: {}' .format(qtde_anuncio))
# print('Quantidade YouTube: {}' .format(qtde_yt_org))
# print('Quantidade IG ou FB: {}' .format(qtde_igfb_org))
# print('Quantidade Site: {}' .format(qtde_site_org))
# print('Quantidade Total Organica: {}' .format(qtde_org))

# arquivo.close

# -------------------------------------------------------------------------------------

#EXERCICIO 2 - ESCREVENDO USANDO O WITH

#AULA 2 - ESCREVENDO EM ARQUIVO COM WITH
arquivo = open('Alunos.txt', 'r')

linhas = arquivo.readlines()

#Deletando as 4 primeiras linhas pois não fazem parte da analise
del linhas[:4]

#Criar indicadores
qtde_anuncio = 0
qtde_yt_org = 0
qtde_org = 0
qtde_igfb_org = 0
qtde_site_org = 0

#Percorrendo arquivo e contando quantidade de cada iteração
for linha in linhas:
    email, origem = linha.split(',')
    if '_org' in origem:
        qtde_org += 1
        if 'hashtag_yt_org' in origem:
            qtde_yt_org += 1
        if 'hashtag_site_org' in origem:
            qtde_site_org += 1
        if ('hashtag_igfb_org' in origem) or ('hashtag_ig_org' in origem):
            qtde_igfb_org += 1
    else:
        qtde_anuncio +=1

with open('Indicadores.txt', 'w') as arquivo_indicadores:
    arquivo_indicadores.write('Quantidade Anuncio: {}\n' .format(qtde_anuncio))
    arquivo_indicadores.write('Quantidade Orgânico: {}\n' .format(qtde_org))
    arquivo_indicadores.write('Quantidade Instagram ou Facebook: {}\n' .format(qtde_igfb_org))
    arquivo_indicadores.write('Quantidade Site: {}\n' .format(qtde_site_org))
    arquivo_indicadores.write('Quantidade YouTube: {}' .format(qtde_yt_org))