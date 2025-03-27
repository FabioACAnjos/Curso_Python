'''crie um programa que leia vários números inteiros.
No final da execução msotre a media entre todos, qual foi o maior e o menos valores lidos.
O programa deve pergutando ao usuário se ele quer ou não continiuar a digitar valores.'''



continuar = 1
c = 0
s = 0
maior = 0
menor = 0
media = 0


while continuar == 1:
    num = int(input('Digite um número inteiro: '))
    c += 1
    s = s + num
    
    if c == 1:
        maior = num
        menor = num
    
    elif num > maior:
        maior = num
    
    elif num < menor:
        menor = num

    continuar = int(input('Digite:\n[1] Se desejar continhar\n[2] Se deseja obter os resultados'))

media = s / c
print('Foram digitados {} valores. \nA média entre eles é {}. \nO maior número digitado foi: {}. \nO menor valor digitado foi: {} ' .format(c, media, maior, menor))

            
