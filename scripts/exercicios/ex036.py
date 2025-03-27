#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual é o valor do imóvel? '))
salario = float(input('Qual é sua renda mensal? '))
tempo = int(input('Em quantos anos você deseja pagar? '))

prestacao = valor // tempo 
limite = salario * 0.3

if prestacao > limite:
    print('Infelizmente o empréstimo foi negado, o valor da prestação ultrapassa 30% da renda')
elif prestacao < limite:
    print('Emprestimo aprovado!')