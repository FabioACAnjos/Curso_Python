#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# matriz = [[],[],[]]

# for c in range(0,3):
#     matriz[0].append(int(input(f'Digite um valor para [0, {c}] ')))

# for c in range(0,3):
#     matriz[1].append(int(input(f'Digite um valor para [1, {c}] ')))

# for c in range(0,3):
#     matriz[2].append(int(input(f'Digite um valor para [2, {c}] ')))

# print(matriz[0])
# print(matriz[1])
# print(matriz[2])

#opção 2

matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]'))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()