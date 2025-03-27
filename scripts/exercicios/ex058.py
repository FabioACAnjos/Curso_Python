'''melhore o jogo do desafio 28 onde o computador vai 'pensar' em um numero  de 0 a 10.... só que agora o jogador vai tentar adivinhar até ele acertar, e mostre no final quantas tentativas foram necessarias'''

#Desafio 28: Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5, e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador;
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

cont = 1

print('Acabei de pensar em um número intero entre 0 e 10, tente adivinhar!!')
computador = randint(0,10)

jogador = int(input('Digite seu palpite: '))

print('Processando ........')
sleep(0.7)

if jogador == computador:
    print('Parabéns você acertou na {}ª chance' .format(cont))
else:
    while jogador != computador :
        jogador = int(input('Que pena você errou. Tente novamente, digite um número: '))
        cont += 1
        print('Processando ........')
        sleep(0.7)

    print('Parabéns você acertou na {}ª chance ' .format(cont))