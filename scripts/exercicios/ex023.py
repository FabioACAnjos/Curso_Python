#Faça um programa que leia um número de 0 a 9999 e nistre ba teka cada um dos dígitos separados

# Ex: digite um número : 1834
# unidade: 4
# dezena:  3
# centena: 8
# milhar: 1


num = int(input('Digite um número de 0 a 9999: '))

# print('milhar:', num[0])
# print('centena:', num[1])
# print('dezena:', num[2])
# print('unidade', num[3])

print('Analisando o número {}'.format(num))
print('unidade {}'.format(num%10))
print('dezena {}'.format(num//10%10))
print('centena {}' .format(num//100%10))
print('milhar {}' .format(num//1000))