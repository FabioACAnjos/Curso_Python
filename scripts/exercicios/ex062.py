'''Melhore o desafio 61, perguntando para o usuário se ele quer mostar mais alguns termos. O programa encerra quando ele disser que quer 0 termos'''

termo = int(input('Digite o primeiro termo: '))
pa = int(input('Digite a P.A Desejada: '))
c = 1

while termo != 0 :
    c = 1
    while c <= 10:
        if termo != 0:
            print('{}'.format(termo), end= ' -> ')
            termo = termo + pa
            c += 1
    print('ACABOU!')    
    print('Gostaria de realizar com outro termo?')
    termo = int(input('Se sim digite o valor, se não digite 0 para sair: '))
    if termo != 0:
        pa = int(input('Digite a P.A Desejada: '))

print('\n\n\nObrigado! ')

