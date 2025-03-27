#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista:', end='')
    for c in range(0, 6):
        lista.append(randint(0, 10))
        print(f' {lista[c]},', end='', flush=True)
        sleep(0.3)


    print('Pronto!')
    
 
def somaPar(lista):
    
    s= cont = 0
    while cont < len(lista):
        if lista[cont] %2 == 0:
            s += lista[cont]
        
        cont += 1

    print(f'Somando os valores pares de {lista}, temos {s}')

numeros = list()

sorteia(numeros)
somaPar(numeros)