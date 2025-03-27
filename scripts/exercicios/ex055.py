# crie um programa que leia o peso de cinco pessoas e mostre o maior e o menor peso lido

cont = 0
maior_peso = 0
menor_peso = 0

for c in range (0, 5):
    cont += 1
    peso = float(input('Digite o peso da {}º pessoa: ' .format(cont)))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print('O maior peso lido foi {:.2f}' .format(maior_peso))
print('O menor peso lido foi {:.2f}' .format(menor_peso))