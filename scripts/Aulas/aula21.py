'''Interactive help'''

'''comando help(), formas de usar, e aparecer as informações. '''
# print('Olá, Mundo!')
# help(print)

# print(input,__doc__)

'''docstrings - seria o passo a passo de como usar a função'''

# def contador(i,f,p):
#     """
#     -> faz uma contagem e mostra na tela.
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c=i
#     while c<= f:
#         print(f'{c}', end='..')
#         c += p
#     print('fim!')

# contador(2,10,2)

# help(contador)

'''Parametro opcional'''

# def somar (a=0,b=0,c=0): #você atribui um valor para o parametro assim não dando erro na função
#     s = a+b+c
#     print(f'A soma vale {s}')


# somar(3,2,5)

# somar(8,4)

'''Escopo de variaveis'''

# def teste():
#     x=8
#     print(f'Na função teste, n vale{n}') # como n está no programa principal, a variável n vai funcionar, pois é uma variável global
#     print(f'Na função teste, x vale {x}')

# #programa principal
# n= 2
# print(f'No programa principal, n vale {n}')
# print(f'No programa principal, x vale{x}') # Nesse caso vai dar erro, pois x é uma variável local,

'''Retorno de valores'''
        #RETURN - é muito util quando queremos ter personalização dos resultados
def somar (a=0,b=0,c=0): #você atribui um valor para o parametro assim não dando erro na função
    s = a+b+c
    #print(f'A soma vale {s}')#retiro o print e adiciono return
    return s

# somar(3,2,5)
# somar(2,2)
# somar(6)

#resp = (somar(3,2,5))#posso colocar o retorno de valor dentro de uma variável
#print(somar(3,2,5))#posso também colocar dentro de um print

#ex:
# r1 = somar(3,2,5)
# r2 = somar(1,7)
# r3 = somar(6)

# print(f'Os meus resultados deram: {r1}, {r2}, {r3}')

'-----------------------------PARTE PRATICA----------------------'

# def fatorial(num=1):
#     f=1
#     for c in range(num, 0, -1):
#         f *= c
#     return f

# # n = int(input('Digite um número: '))
# # print(f' O fatorial de {n} é igual a {fatorial(n)} ')

# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os Resultados são {f1}, {f2}, {f3}')

'''Retorna qualquer valor, como lógico, num, str..'''

def par(n=0):
    if n %2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
#print(par(num))

#ou

if par(num):
    print('É par')
else:
    print('Não é par')