#Faça um programa que leia o nome completo de uma pessoa e em seguida mostre o primeiro e o último nome separadamente

nome = str(input('Digite seu nome completo: '))

nome_div = nome.split()

print(nome_div)

print('Nome: {}'.format(nome_div[0]))

print('Último nome: {}' .format(nome_div[len(nome_div)-1]))

print(len(nome_div))