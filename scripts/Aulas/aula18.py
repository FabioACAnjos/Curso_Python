# teste = list()

# teste.append('Gustavo')
# teste.append(40)

# galera = list()
# galera.append(teste[:]) #[:] cria uma cópia da lista

# teste[0] = 'maria'
# teste[1] = 22

# galera.append(teste[:])
# print(galera)


galera = [['joão', 19], ['ana', 33] ,['Joaqui', 13] ,['Maria' , 45]]

# print(galera[2][1])

# for p in galera:
#     print(p[1])

galera = list()

dado = list()

totmai = totmen = 0

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    
# print(galera)
# print(dado)

#Pessoas acima de 21:

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
        
print(f'Temos {totmai} maiores e {totmen} menores de idade.')