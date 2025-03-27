#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
somacoluna = 0
maiorl2 = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para a posição [{l}, {c}] '))

        if matriz[l][c] %2 ==0:
            par += matriz[l][c]

    #opção 1 soma de coluna e maior número
        # if c == 2:
        #     somacoluna += matriz[l][c]

        # if l == 1 and c == 0:
        #     maiorl2 = matriz [l][c]
        # if matriz[1][c] > maiorl2:
        #     maiorl2 = matriz[l][c]



for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()
#opção 2 soma de coluna e maior numero
for l in range(0,3):
    somacoluna += matriz[l][2]

for c in range(0,3):
    if c == 0 or matriz[1][c] > maiorl2:
        maiorl2 = matriz[1][c]

print(f'A soma dos valores pares digitados foi {par}')
print(f'A soma dos valores da terceira coluna é {somacoluna}')
print(f'O maior digita na segunda linha foi {maiorl2}')