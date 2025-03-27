

#ex de aula

 # Em portugol #
'''enquanto não maça
    se tiver chão
        passo
    se tiver buraco
        pula    
    se tiver moeda
       pega
pega'''

# em python #

'''while not maça:
    if chão:
        passo
    if buraco:
        pula
    if moeda
        pega
pega'''

# com for #
for c in range (1,10):
    print(c)
print ('Fim')

# Com While #

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

# Enquanto não digitar o 0 o programa continua

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar +=1


print('Você digitou {} numeros pares e {} numeros impares ' . format(par, impar))