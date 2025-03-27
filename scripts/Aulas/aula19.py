#Dicionário


# pessoas = {'nome': 'Gustavo', 'sexo' : 'M', 'idade' : 22}

# print(f' o {pessoas["nome"]} tem {pessoas["idade"]} anos')

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# #repetições
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# #para modificar
# pessoas['nome'] = 'Leandro'

# #para adicionar
# pessoas['peso'] = 98

# #criar um dicionário dentro de uma lista
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla' : 'SP'}

# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[0]['uf'])
# print(brasil[1]['sigla'])

#ler e adicionado no dicionário e adicionar na lista. (copiar o elemento)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
# print(brasil)

# for Estado in brasil: #for para lista
#     for uf, sigla in Estado.items():
#         print(f'O Campo {uf} tem valor {sigla}')

for Estado in brasil: #for para lista
    for valor in Estado.values():
        print(valor, end=' ')
    print()