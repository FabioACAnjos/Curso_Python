# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# para salários superiores a R$ 1.250,00 calcule um aumento de 10%
# para inferiores ou iguais o aumento é de 15%


sal = float(input('Digite seu salário: '))

if sal > 1250 :
    print('Seu salário terá um aumentod e 10%, ficando no valor de R$ {:.2f}' .format(sal*1.1))
else:
    print('Seu salário terá um aumento de 15%, ficando no valor de R$ {:.2f}' .format(sal * 1.15))
