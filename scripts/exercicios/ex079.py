#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


lista_numeros = []
digitado = 0
continuar = 'S'

while continuar == 'S':
    digitado = (int(input('Digite um valor inteiro: ')))
    if lista_numeros.count(digitado) > 0:
        print(f'Numero já adicionado, não vou adicionar...')
        
    else:
        lista_numeros.append(digitado)
        print(f'Valor adiconado com sucesso...')
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    
    
lista_numeros.sort()    
print(lista_numeros)


# numeros = list()

# while True:
#     n = int(input('Digite um número inteiro: '))
#     if n in numeros:
#         print('Valor duplicado, não irei adicionar...')
#     else:
#         numeros.append(n)
#         print('Valor adicionado com sucesso...')

#     continuar = str(input('Quer continuar? [S/N] '))
#     if continuar in 'Nn':
#         break
# numeros.sort()
# print(numeros)