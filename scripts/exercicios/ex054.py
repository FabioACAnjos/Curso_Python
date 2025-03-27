# crie um programa que leia o ano de nascimento de sete pessoas, no final mostre quantas são maiores e quantas não são. (cosiderando 21 anos)

import datetime

ano_atual = datetime.date.today().year
idade = 0
maior = 0
menor = 0
cont = 0

for c in range (0, 7):
    cont += 1
    nascimento = int(input('Digite o ano de nascimento da {}º pessoa: ' .format(cont)))
    idade = ano_atual - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1


print('Das {} pessoas inseridas {} são maiores de idade e {} são menores de idade' .format(cont, maior, menor))    