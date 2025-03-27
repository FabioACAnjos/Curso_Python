##Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha (NOME = '<DESCONHECIDO>', GOLS = 0):
    
      
    print(f'O Jogador {NOME} fez {GOLS} gols(s) no campeonato.')
    



#programa principal

nome = str(input('nome do Jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() =='':
    ficha(GOLS= gols)
else:
    ficha(nome , gols)


