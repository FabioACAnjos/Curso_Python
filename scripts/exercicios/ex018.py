#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o valor do angulo: '))


seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('O seno de {:.0f} é {:.3f}' .format(angulo, seno))
print('O cosseno de {:.0f} é {:.3f}'. format(angulo, coss))
print('A tangênte de {:.0f} é {:.3f}' .format(angulo, tang))