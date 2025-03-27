'''faça um programa que leia um número qualquer e mostre o seu fatorial (fazer com while e com for)'''

num = int(input('Digite um número inteiro para descobrir seu fatorial: '))
fatorial = num
cont = num

while cont > 1 :
    fatorial = fatorial * (cont-1)
    cont -= 1
    

print('O fatorial de {} é igual à: {}' .format(num, fatorial))
