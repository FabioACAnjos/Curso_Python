# crie um programa de jokenpô

import random
import time
itens = ['Pedra', 'Papel' , 'Tesoura']
print('====== Jogo do Jokenpô =====')
print('Escolha sua opção:')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')

jogador = int(input('Qual a sua jogada? '))

computador = random.choice(itens)
time.sleep(1)
print('\n.....Jo.....\n')
time.sleep(1)
print('.....Ken....\n')
time.sleep(1)
print('.....Pô.....\n')
time.sleep(1)
if jogador == 1: #escolha do jogador pedra
    print('Jogador escolheu: Pedra')
    if computador == 'Pedra':#Condição de empate
        print('Computador escolheu: {}'.format(computador))
        print('\nxxxx Empate xxxx\n')
    elif computador == 'Papel': #Condição de derrota
        print('Computador escolheu: {}'.format(computador))
        print('\nxxxx Você Perdeu! xxxx\n')
    else: #Condição de vitória
        print('Computador escolheu: {}'.format(computador))
        print('\nxxxx Você Ganhou! xxxx\n')

elif jogador == 2: #Escolha do jogador Papel.
    print('Jogador escolheu: Papel')
    if computador == 'Papel': #Condição de empate
        print('Computador escolheu: {}'.format(computador))
        print('\nxxxx Empate xxxx\n')
    elif computador == 'Tesoura': #Condição de derrota
        print('Computador escolheu: {}'.format(computador))
        print('\nxxxx Você Perdeu! xxxx\n')
    else: #Condição de vitória
         print('Computador escolheu: {}'.format(computador))
         print('\nxxxx Você Ganhou! xxxx\n')

elif jogador == 3 : #Escolha do jogador Tesoura
    print('Jogador escolheu: Tesoura')
    if computador == 'Tesoura':#Condição de empate
        print('Computador escolheu: {}'.format(computador))
        print('\nxxxx Empate xxxx\n')
    elif computador == 'Pedra': #Condição de derrota
        print('Computador escolheu: {}'.format(computador))
        print('\nxxxx Você Perdeu! xxxx\n')
    else: #Condição de vitória
        print('Computador escolheu: {}'.format(computador))
        print('\nxxxx Você Ganhou! xxxx\n')

else:
    print('Opção inválidade, escolha novamente')