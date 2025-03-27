# Desenvolva um programa que leia o comprimento de três retas e diga se ele pode ou não formar um triângulo.

l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))

if (l1+l2) > l3 and (l1+l3) > l2 and (l3+l2) > l1:
    print('É poossível formar um triângulo')
else:
    print('Não é possível formar um triângulo')

