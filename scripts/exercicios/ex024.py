#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"


ncid = str(input('Digite o nome da cidade: '))

dividido = (ncid.split())

print(dividido[0].upper() == 'SANTO' )


#Segunda opção

ncid = str(input('Digite o nome da cidade: ')).upper().strip()

print(ncid[:5] == 'SANTO')

