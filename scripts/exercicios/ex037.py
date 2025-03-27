#Escreva um programa que leia um n´pumero inteiro qualquer e peça para o usuário escolher qual será a base de conversão
# 1 para binário
# 2 para octal
# 3 para hexadecimal


num = int(input('Digite um número inteiro: '))

escolha = int(input('Escolha a base de conversão: \n[1]converter para binário\n[2]converter para octal\n[3]converter para Hexadecimal\nSua opção: '))

if escolha == 1:
    print('{} convertido para binário é igual a {}' .format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para octal é igual a {}' .format(num , oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}' .format(num , hex(num)[2:]))
else:
    print('Opção invalida')