# Escreva um programa que leia dois números inteiros e compare-os,. mostrando na tela a uma mensagem
# - O primeiro valor é maior
# - o Segundo valor é maior
# - Nãoi existe valor maior os dois são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro valor é o maior')

elif num2 > num1:
    print('O segundo numero é maior')

elif num1 == num2:
    print('Não existe valor maior os dois são iguais')