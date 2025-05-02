import uteis
import uteis.operacoes

p = float(input("Digite o preço: "))

print(f'A metade de {p} é {uteis.operacoes.metade(p)}')

print(f'O dobro de {p} é {uteis.operacoesoperacoes.dobro(p)}')

print(f'Aumentando 10%, temos {uteis.operacoes.aumentar(p, 10)}')

print(f'Reduzindo 13%, temos {uteis.operacoes.diminuir(p, 13)}')