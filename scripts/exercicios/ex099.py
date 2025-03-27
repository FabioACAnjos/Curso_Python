#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* num):
    print('=-' *20)
    print('Analisando os valores passados....')

    cont = 0
    m = 0
    for valores in num:
        print(f' {valores},', end='', flush=True)
        sleep(0.3)

        if m < valores:
            m = valores
        cont += 1

    print(f' Foram analisdos {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}.')

    print('=-' *20)





#principal :

maior (2,9,4,5,7,1)
maior (1,30,2,54,23,125)