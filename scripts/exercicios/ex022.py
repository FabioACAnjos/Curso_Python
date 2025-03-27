#Crie um programa que leia o nome completo de uma pessoa e mostre:
#   - O nome com todas as letras maiúsculas
#   - O nome com todas as letras minúsculas
#   - Quantas letras ao todo (sem considderar os espaços)
#   - Quantas letras tem o primeiro nome


nome = str(input('digite seu nome completo: '))

print('Maiúsculo:', nome.upper())
print('Minúsculo:', nome.lower())
print('Total de letras:', len(nome.replace(' ','')))
dividido = nome.split()
print('Qtd de letras no 1º nome:', len( dividido[0] ) )
