# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


lista_num = list()

for c in range(0,5):
    digitado = int(input('Digite um valor inteiro: '))
    if c == 0 or digitado > lista_num[len(lista_num)-1]:
        lista_num.append(digitado)
    
    else:
        pos = 0
        while pos < len(lista_num):
            if digitado <= lista_num[pos]:
                lista_num.insert(pos, digitado)
                break
            pos += 1

print(lista_num)

