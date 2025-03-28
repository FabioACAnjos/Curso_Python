#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

partidas = []
jogador = {
    'nome':'',
    'gols' : '',
    'total': 0
}


jogador['nome'] = str(input('Nome do jogador: '))
npartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

cont = 0

while cont < npartidas:
    ngols = int(input(f'Quantos gols na partida {cont}? '))
    partidas.append(ngols)
    cont += 1

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('=-'*20)

print(jogador)

print('=-'*20)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('=-'*20)

print(f'O jogador {jogador["nome"]} jogou {npartidas} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols')