#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


lista1 = list()
listaPar = list()
listaImp = list()

while True :
    n=(int(input('Digite um valor: ')))
    lista1.append(n)
    
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImp.append(n)
    
    continuar = str(input('Deseja Continuar? [S/N] '))
    
    if continuar not in 'Ss':
        break

print(f'A lista de todos os numeros gerados é :{lista1}.\nA lista dos números pares gerada é {listaPar}. \nA Lista dos números impares gerada é {listaImp}')
    