#melhor forma de usar para não gerar conflito
import PacoteUteis
import PacoteUteis.PacoteNumeros

num = int(input('Digite um valor: '))
fat = PacoteUteis.PacoteNumeros.fatorial(num)

print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {PacoteUteis.PacoteNumeros.dobro(num)}')
print(f'O Triplo de {num} é {PacoteUteis.PacoteNumeros.triplo(num)}')

# OU


# from uteis import fatorial, dobro, triplo

# #principal

# num = int(input('Digite um valor: '))
# fat = fatorial(num)

# print(f'O fatorial de {num} é {fat}.')
# print(f'O dobro de {num} é {dobro(num)}')
# print(f'(O Triplo de {num} é {triplo(num)})')

#um pacote é a junção de modulos separados por assunto (uma pasta que contem modulos)


'''para criar pacotes é só criar uma pastas
    para cada pasta precisa criar o arquivo __init__.py


'''