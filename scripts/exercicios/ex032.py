#Faça um progrma que leia um ano qualquer e mostre se ele é bissexto.
#


ano = int(input('Digite o ano desejado: '))
if ano%100 != 0 and ano%4 == 0:
    print('O ano {} é bissexto' .format(ano))
    
else:
    if ano%400 == 0:
        print('O ano {} é bissexto' .format(ano))
      
    else:
        print('O ano {} não é bissexto' .format(ano))
