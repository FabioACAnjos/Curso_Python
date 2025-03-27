#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
# a) de 1 até 10, de 1 em 1                                                                                                                                              
# b) de 10 até 0, de 2 em 2                                                                                                                                           
# c) uma contagem personalizada

from time import sleep

def contador(inicio , fim, passo):
    print('=-' *20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    print('=-' *30)
    if passo < 0 :
      passo *=  -1
    if passo == 0:
        passo = 1
        
    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f' {c},', end='')
            
            c += passo
        print('Fim!')    

    else:
        c = inicio
        while c >= fim:
            print(f' {c},', end='')
        
            c -= passo
        print('Fim!')



#Programa pincipal

# A) de 1 até 10, de 1 em 1

contador(1, 10, 1)

# B) de 10 até 0, de 2 em 2

contador(10, 0, 2)

# C) uma contagem personalizada
print('=-' *30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Digite o valor inicial: '))
f = int(input('Digite o valor final: '))
p = int(input('Digite o passo: '))

contador(i, f, p)
