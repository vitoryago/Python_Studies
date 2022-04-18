#AULA 1: STRINGS - TAMANHO DA STRING

text = 'Olá, como você está?'
print(len(text))
print(text[5])

AULA 2: INDICES STRING
text = 'Olá, tudo bem com você?'
# print(text[-1])
# print('Gostaria de fazer um teste e imprimir essa variável: ' + text)
faturamento = 500
lucro = 500
print('O faturamento foi {0}, lucro {1}, faturamento {0}' .format(faturamento, lucro))
recebe = '@' in 'vitor@com'
print(recebe)

# #AULA 3: MÉTODO STRING

texto = 'olá como você está?'
texto_up = 'OLÁ COMO VOCÊ ESTA'

print(texto.title())

#AULA 4: EXERCÍCIO - CPF

cpf = input('Digite seu CPF: ')
cpf = cpf.strip()
cpf = cpf.replace('.','')
cpf = cpf.replace('-','')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Digite seu CPF corretamente.')

#AULA 5: EXERCICIO NOME E EMAIL

nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
pos_a = email.find('@')
servidor = email[pos_a:]

if nome and email and pos_a != -1 and servidor.find('.') != -1:
    print(nome + ' ' + email)
else:
    print('email incorreto')

#AULA 6: FORMATAÇÃO DE STRINGS

email = 'vitor@gmail.com'
lucro = -2000
faturamento = 1000
# print('Meu email não é {:^30}, entendeu?' .format(email))
print('faturamento de {:+,.1f} lucro de {:+,.1f}' .format(lucro,faturamento))