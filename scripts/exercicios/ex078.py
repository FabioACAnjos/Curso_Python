
#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num = []

for c in range(0,5):
    num.append(int(input(f'Digite o valor na posição {c} ')))

maior = menor = num[c]
maior = max(num)
menor = min(num)

print('=-'*40)   
print(f'O Maior valor digitado foi {maior} nas posições ', end='')

for c, v in enumerate(num):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f'O Menor valor digitado foi {menor} nas posições ', end='')
for c, v in enumerate(num):
    if v == menor:
        print(f'{c}...', end='')
print()
print('=-'*40) 
