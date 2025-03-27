'''Refaça o 51, com while'''

# crie um programa que leia o primeirop termo e a razão de uma prograssão aritmetica (PA), no final mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
pa = int(input('Digite a P.A Desejada: '))
c = 1

while c <= 10:
    print('{}'.format(termo), end= ' -> ')
    termo = termo + pa
    c += 1

print('ACABOU!')