'''Crie um programa que leia vários núimeros inteiros pelo teclado, O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

s = 0
c = 0
digitado = 0
while digitado != 999:
    num = int(input('Digite um número para ser somado (caso queira parar digite 999): '))
    digitado = num
    if num/999 == 1:
        print ('Foram digitados {} numeros e a soma de todos resulta no valor {}' .format(c, s))
        
    else:    
        s = s + num
        c += 1

print('Fim')