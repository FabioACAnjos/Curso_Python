# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, 
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.



dados = list()
pessoas = list()
maiorpeso = 0
menorpeso = 0

while True:
    #input de dados
    print()
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    print('=-' *30)
    print()
    #descobrir o maior e menor peso
    if len(pessoas) == 0 :
       maiorpeso = dados[1]
       menorpeso = dados[1]
    
    if dados[1] > maiorpeso:
       maiorpeso = dados[1]
    
    if dados[1] < menorpeso:
       menorpeso = dados[1]

    #nova lista de armazenamento
    pessoas.append(dados[:])
    #limpando a primeira lista a cada passagem
    dados.clear()

    continuar = str(input('Deseja inserir outra pessoa? [S/N] '))
    if continuar not in 'Ss':
      break  
    print('=-' *30)

print(f'Foram cadastradas {len(pessoas)} no sistema.')
print(f'O maior peso digitado foi {maiorpeso}Kg. que é o peso de: ', end='')
for c in pessoas :
   if c[1] == maiorpeso:
      print(f'{c[0]}', end='; ')

print()
print(f'O Menor pesso cadastrado foi {menorpeso}Kg. que é o peso de: ', end='')
for c in pessoas :
   if c[1] == menorpeso:
      print(f'{c[0]}',end='; ')

print()


