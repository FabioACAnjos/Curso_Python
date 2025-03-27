
#Em Portugol#
''''enquanto verdadeiro
    se piso
        anda
    se vazio
        pula
    se moeda
        pega
    se trofeu
        pula
        interrompa
pega'''

#Em Python#
''' while true 
    if piso
        passo
    if vazio
        pula
    if moeda 
        pega
        break
pega'''

#forma tradicional
# cont = 1
# while cont <=10:
#     print(cont, '->', end=' ')
#     cont += 1

# print ('Acabou')

#com essa alteração vira um loop infinito
# cont = 1
# while True:
#     print(cont, '->', end=' ')
#     cont += 1

# print ('Acabou')


#loop com break

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break

    s += n

#print ('A soma vale {}' .format(s))


#FSTRING

print ('A soma vale {}' .format(s)) #forma antiga
print(f'A soma vale {s}')