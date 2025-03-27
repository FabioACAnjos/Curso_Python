# crie um programa que leia nome, idade e sexo de 4 pessoas, no final o programa deve mostrar 
# - a media de idade do grupo
# - qual é o nome do homem mais velho
# - quantas mulheres tem menos de 20 anos

import os

# variáveis
soma_idade = 0
nome_hmv = ''
idade_hmv = 0
cont_mulher = 0

#loop para 4 pessoas
for c in range(1, 5):
    #criando base de dados:
    nome = str(input('Digite o nome da {}ª pessoa: ' .format(c))).strip()
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    idade = int(input('Digite a idade: '))
    print('\n')

    #somando as idades de todas as pessoas:
    soma_idade += idade

    # Caso seja homem descobrir o homem mais velho:
    if sexo == 'M':
        if c == 1: # para a primeira passagem do loop, adicionamos o primeiro dado as var. abaixo.
            idade_hmv = idade
            nome_hmv = nome
        else: # Nas demais passagens do loop o alg irá verificar se a idade digitada do homem é maior que a idade já armazenada
            if idade > idade_hmv:
                idade_hmv = idade
                nome_hmv = nome

    # Contagem das mulheres acima de 20 anos
    if sexo == 'F':
        if idade > 20 :
            cont_mulher += 1

    os.system('clear')



idade_media = soma_idade / 4

print('A idade media do grupo é {}' .format(idade_media)) 
print('O homem mais velho digitado foi {} com {} anos' .format(nome_hmv, idade_hmv))
print('Foi digitado um total de {} mulheres com mais de 20 anos' .format(cont_mulher))