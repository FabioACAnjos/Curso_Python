# Refaça o desafio 9 mostrando a tabuada de um numero que o usuário escolher só que agora utilizando um laço for.

num = int(input('Digite um número para ver sua tabuada: '))

for c in range (0, 11):  
    print('{} x {} = {}' .format(num, c, num*c))

print('Acabou')

