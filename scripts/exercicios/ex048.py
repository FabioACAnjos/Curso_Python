# crie um programa que mostre na tela calcule a soma entre todos os numeros impares  que são multilplos de três que se encontram no intervalo de 1 e 500


s = 0
for c in range(1, 501):
    if c %2 == 1 and c %3 == 0:
        s += c

print('A somatória é {}' .format(s))