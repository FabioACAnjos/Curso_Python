#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

#cálculo da hipotenusa

hip = math.sqrt (pow(co,2) + pow(ca,2))

print('A hipotenusa é: {:.2f}' .format(hip) )
print('A hipotenusa é: {:.2f}' .format(math.hypot(co,ca) ))