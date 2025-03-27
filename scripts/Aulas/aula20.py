'''funções são rotinas de execução

usa a sigra def

por exemplo mostar a linha:
'''

#Função sem parametro
# def mostralLinha():
#     print('=-'*30)

# #exemplo
# mostralLinha()
# print('            Sistema de Alunos          ')
# mostralLinha()
# print('           Cadastro de Funionários         ')
# mostralLinha()


# #também pode ser usado com parametros

# def título(txt):
#     print('=-'*30)
#     print(txt)
#     print('=-'*30)

# título('Sistema de Alunos')
# título('Curso em Vídeo')

# #Parte prática
# def soma(a,b):
#     s = a + b
#     print(s)


# #programa principal
# soma(4, 5)
# soma(8, 9)
# soma(2, 1)

# '''Conceito empacotar parametros
# exemplo 

# def contador (*num): #o asteristico significa desempacotar

# contador (5,7,3,1,4)
# contador (8,4,7)
# '''

# def contador(*num):
#     for valor in num:
#         print(f'{valor} ', end='')
#     print('Fim!')



# contador (2,1,7)
# contador (8,0)
# contador (4,4,7,6,2)


#trabalhando com listas

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos]*=2
#         pos += 1

# #programa principal
# valores = [7,2,5,0,4]

# dobra(valores)
# print(valores)

#como desempacotar valores
def soma(*valores):
    s=0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5,2)
soma(2,9,4)