# Crie um algoritmo que leia um número e mostre o seu dobre, triplo e a raiz quadrada
import math

n = int(input('Digite um número: '))

print('Você digitou o número {},\n o seu dobro é {},\n o seu triplo é {},\n a sua raiz quadrada é {:.2f}' .format(n, n*2, n*3, math.sqrt(n)))