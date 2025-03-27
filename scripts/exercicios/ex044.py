# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
# a vista = dinheioro / cheque 10% de desconto
# a vista no cartão 5% de desconto
# ate 2x nor catão preço normal
# 3x ou mais no cartão 20% de juros


preco = float(input('coloque o valor total das compras: '))

print('==== Escolha a forma de pagamento ===')
print('[1] À vista em dinheiro ou cheque')
print('[2] À vista no cartão')
print('[3] 2x  no cartão')
print('[4] 3x ou mais no cartão')
escolha = int(input('Qual é a opção? '))

if escolha == 1:
    n_preco = preco - (preco*0.10 )
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final '.format(preco, n_preco))
elif escolha == 2:
    n_preco = preco - (preco*0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final '.format(preco, n_preco))
elif escolha == 3:
    parcela = preco / 2
    print('Sua compra de R${:.2f} será paga em 2 parcelas de R${:.2f}' .format(preco, parcela))
elif escolha == 4:
    n_preco = preco*1.2
    parcela = int(input('Quantas parcelas? '))
    valor_parcela = n_preco / parcela
    print('Sua compra de R${:.2f} vai custar R${:.2f} em {}x de R${:.2f} '.format(preco, n_preco, parcela, valor_parcela))