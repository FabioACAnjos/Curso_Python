#
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#

num1 = int(input('digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3 and num2 > num3:
    print('O maior número digitado foi {} e o menor foi {}' .format (num1 , num3))

