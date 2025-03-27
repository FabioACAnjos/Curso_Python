# crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

import math

n_real = float(input('Digite um valor real: '))
# n_int = math.floor(n_real)

print('Você digitou o número real {}, e a sua parte inteira é {}' .format(n_real, math.floor(n_real)))
print('Você digitou o número real {}, e a sua parte inteira é {}' .format(n_real, math.trunc(n_real)))
