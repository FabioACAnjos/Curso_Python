# crie um programa que leia uma frase qualquer e diga se ela é um palindromo (que da para ler da frente pra frente e fica igual) 
# ex: apos a sopa
# a sacada da casa
# a torre da derrota

frase = str(input('Digite a frase: '))
junta = frase.strip().replace(' ', '')
nfrase = ''

for c in range (len(junta)-1, -1, -1):
    nfrase += junta[c]    

if nfrase == junta:
    print('A frase "{}" é um palindromo'.format(frase))
else:
    print('A frase "{}" não é um palindormo' .format(frase))