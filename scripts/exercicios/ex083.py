#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = list()

expressao = str(input('Digite a expressão: '))

aberto = expressao.count('(')    
fechado = expressao.count(')')


print(aberto)
print(fechado)

if aberto == fechado:
    print('A expressão é valida')
else:
    print('Expressão incorreta')