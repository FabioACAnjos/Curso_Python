#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média


soma = 0 
pessoas = list()
dados = {
    'nome': '',
    'sexo': '',
    'idade': 0,
}

while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: '))
    if dados['sexo'] not in 'MmFf':
           while dados['sexo'] not in 'MmFf':
                print('ERRO! Responda apenas M ou F.')
                dados['sexo'] = str(input('Sexo [M/F]: '))
     


    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']

    pessoas.append(dados.copy())

    continuar = str(input('Quer continuar? [S/N] '))
    if continuar not in 'NnSs':
            while True:
                print('ERRO! Responsa apenas S ou N.')
                continuar = str(input('Quer continuar? [S/N] ')) 

                if continuar in 'NnSs':
                      break
    
    if continuar in 'Nn':
            break
    

#Item A, total de pessoas cadastradas
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

#item B, a média de idade
media = soma / len(pessoas)
print(f'B) A média de idade é de {media:5.2f}.')

#Item C, Uma lista com as mulheres
print('C) as mulheres cadastradas foram ', end='')
for pessoa in pessoas:
   if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]}', end=' ')

print()
print(f'D) Lista de pessoas que estão acima da média:')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        for k, v in pessoa.items():
            print(f'{k} = {v};', end='')
        print()
