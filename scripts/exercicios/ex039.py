# faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: 
# - se ele ainda vai se alistar ao serviço militar 
# - se é a hora de se alistar 
# - se já passou do tempo do alistamento. 
# O programa deve mostrar também o tempo que passou ou o tempo que falta.

import datetime
print('Alistamento militar!')

nasc = int(input('Digite o seu ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - nasc
ano_alist = nasc + 18

if idade > 18 : 
    prazo = atual - ano_alist
    print('Quem nasceu em {} tem {} anos em {}' .format(nasc, idade, atual))
    print('você já deveria ter se alistado há {} anos' .format(prazo))
    print('Seu alistamento foi em {}' .format(nasc+18))

elif idade < 18 :
    prazo = ano_alist - atual
    print('Quem nasceu em {} tem {} anos em {}' .format(nasc, idade, atual))
    print('Você tem que aguardar {} anos para se alistar' .format(prazo))
    print('Você deverá se alistar em {}' .format(ano_alist))

else:
    print('Você tem {} este ano é quando você deve se alistar'. format(idade))