#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem cobrando R$0,50 por Km para viagens até 200Km e R$ 0,45 para viagens mais longas.


dist = float(input('Digita a distância a ser percorrida em km: '))

if dist > 200 :
    print('O valor da passagem é R$ {:.2f}' .format(dist*0.45))

else:
    print('O valor da passagem é R$ {:.2f}' .format(dist * 0.50))