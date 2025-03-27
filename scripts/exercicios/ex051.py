# crie um programa que leia o primeirop termo e a razão de uma prograssão aritmetica (PA), no final mostre os 10 primeiros termos dessa progressão.

inicio = int(input('Digite o primeiro termo: '))
pa = int(input('Digite a P.A desejada: '))
fim = (pa*10)+inicio

for c in range( inicio, fim, pa):
     print('{}'.format(c), end=' -> ')

print ('ACABOU')