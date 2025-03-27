#categorias de aluno de acordo com a idade 
# - até 9 anos mirim
# - ate 14 anos infantil 
# - até 19 anos junior 
# - até 20 anos sênio 
# - acima master

import datetime

nasc = int(input('Qual o ano de nascimento do atleta? '))
atual  = datetime.date.today().year
idade  = atual - nasc

print('O atleta tem {} anos.'.format(idade))
if idade <= 9 :
    print('Classifação : Mirim')
elif idade <= 14 :
    print('Classifação : Infantil')
elif idade <= 19 :
    print('Classifiação : Junior')
elif idade <= 25 :
    print('Classificação: Sênior')
else:
    print('Classifação : Master')
