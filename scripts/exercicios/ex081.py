#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

num = list()

while True:
    num.append(int(input('Digite um valor: ')))
    
    continuar = str(input('Deseja Continuar? [S/N] '))
    
    if continuar not in 'Ss':
        break

print('=-'*30)
print(f'Foram digitados {len(num)} números')
num.sort(reverse=True)
print(f'A lista de forma ordenada fica = {num}')

if 5 in num:
    print('O valor 5 está contido na lista')
else:
    print('O valor 5 não esta contido na lista')
