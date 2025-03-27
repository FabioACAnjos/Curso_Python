'''faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F, caso esteja errado, peça a digitação novamente até ter um valor correto'''


sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()

while sexo not in 'MF' :
    sexo = str(input('Dados invalidos. Por favor digite o sexo [M/F] ')).strip().upper()
   
print('Obrigado!')
print('------FIM--------')