#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.



# def voto(a):
#     from datetime import date
#     idade = date.today().year - a

#     if idade < 16:
#         print(f'Com {idade} anos: Voto NEGADO.')
#     elif 16 <= idade < 18 or idade > 70 :
#         print(f'Com {idade} anos: Voto OPCIONAL.')
#     else:
#         print(f'Com {idade} anos: Voto OBRIGATÍRIO.')

# #programa principal
# print('-'*30)

# nascimento = int(input('Em que ano você nasceu? '))

# voto(nascimento)


'''OU'''

def voto(a):
    from datetime import date
    idade = date.today().year - a

    if idade < 16:
        return(f'Com {idade} anos: Voto NEGADO.')
    elif 16 <= idade < 18 or idade > 70 :
        return(f'Com {idade} anos: Voto OPCIONAL.')
    else:
        return(f'Com {idade} anos: Voto OBRIGATÍRIO.')

#programa principal
print('-'*30)

nascimento = int(input('Em que ano você nasceu? '))

voto(nascimento)
print(voto(nascimento))