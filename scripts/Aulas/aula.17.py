# num = [2, 5, 9, 1]

# num.append(7) #adicionar no fim da lista

# num.sort(reverse=True) #ordenar de forma reversa
# num.insert(2,0) #inserir valor 0 na posição 2

# num.pop(2) #remove o valor na posição 2

# num.remove(4) #irá remover o primeiro numero quatro encontrado.

# print(num)

# enumerate(valor) #retornar além do valor a posição ex:

# valores = [5 , 9, 4]

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}')

# print('Cheguei no fim da lista')


a = [2 , 3, 4 , 7]
# b = a #Dessa forma se cria uma ligação, tudo que mudar em uma lista muda na outra
b = a[:] #Dessa forma se cria uma cópia da lista A em B, os valores mudados em B não alteração em A
b[2] = 8
print(f'Lista A : {a}')
print(f'Lista B : {b}')