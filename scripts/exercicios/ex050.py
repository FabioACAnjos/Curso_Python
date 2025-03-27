# crie um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares, se for impar desconsiderar
s = 0

for c in range (1 , 7):
    num = int(input('Digite o {}º número inteiro: '.format(c)))
    if num % 2 == 0:
        s += num

print('A soma dos números pares digitados é {}'.format(s))