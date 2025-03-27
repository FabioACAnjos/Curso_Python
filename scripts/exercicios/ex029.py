#Escreva um programa que leia a velocidade de um carro,
#Se ele ultrapassar 80km/h, mostre a mensagem que ele foi multado
#mostrar o valor da multa, ela vai custar R$7,00 para cada km acima do limite.



vel = float(input('Digite a velocidade do carro: '))

if vel > 80 : #teste para saber se está acima da velocidade máxima de 80km/h
    print('Você excedeu o limite de velocidade, por isso foi multado.') 
    multa = ((vel - 80) * 7) #Calcula o valor da multa
    print('O valor da multa é: R$ {:.2f}' .format(multa))