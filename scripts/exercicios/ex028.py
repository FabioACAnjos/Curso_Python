#Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5, e paça para o usuário tentar descobrir qual foi o número escolhido pelo computador;
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random # importa a biblioteca randomica
import time # importa a biblioteca de processos de tempo
num = random.randint(0,5) #Gera um número de forma randomica no intervalor de 0 a 5

#print(num)

num2 = int(input('Tente acertar o valor de 0 a 5 que o computador gerou. \n Digite o número: ')) 
print('Processando ....')
time.sleep(3)
if num == num2 :
    print('Parabéns, você venceu!')
else:
    print('Que pena, você perdeu!')