#Crie um progmra que leia um número inteiro e mostre na tela se ele é par ou impar
#

num = int(input('Digite um número inteiro: '))

if num %2 == 0:
    print('O número {} é par' .format(num))
else:
    print('O número {} é impar' .format(num))