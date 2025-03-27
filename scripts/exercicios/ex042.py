#faça o 35 e diga se o triângulo é 
# equilátero - todos os lador iguais 
# isósceles - dois lados iguais
# escaleno - todos os lados diferentes

l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))

if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
        print ('Com essas medidas é possível fazer um triângulo.')
        if l1 == l2 == l3:
         print('O triângulo é equilátero')
        elif l1 != l2 != l3:
         print('O triângulo é escaleno')
        else:
         print('O triângulo é isósceles')
else:
    print('Não é possível formar um triângulo')
