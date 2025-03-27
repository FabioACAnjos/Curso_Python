#Programa da média do aluno - media abaixo de 5 reprovado - entre 5 e 6.9 recuperação - media acima de 7 aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)//2

if media < 5:
    print('Sua média foi de {}, você está reprovado'.format(media))
elif media >=5 and media < 7 :
    print('Sua média foi de {}, você está em recuperção' .format(media))
elif media > 7 and media <= 10:
    print('Sua média foi de {}, parabéns você está aprovado!'.format(media  ))
else:
    print('Houve algum erro pois a média é {}, por favor inserir os dados novamente'.format(media))