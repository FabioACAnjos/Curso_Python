#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


dados = {'NOME': '', 'MEDIA': 1, 'SITUACAO':''}

print('=-' *20)
dados['NOME'] = str(input('Nome: '))
dados['MEDIA'] = float(input(f'Média de {dados["NOME"]}: '))
print('=-' *20)

if dados['MEDIA'] >= 7.0 and dados['MEDIA'] <=10.0:
    dados['SITUACAO'] = 'APROVADO'
elif dados['MEDIA'] < 7 and dados['MEDIA'] >= 4.5:
    dados['SITUACAO'] = 'RECUPERAÇÃO'
elif dados['MEDIA'] >=0 and dados['MEDIA'] < 4.5:
    dados['SITUACAO'] = 'REPROVADO'




print(f'- nome é igual a {dados["NOME"]}')
print(f'- média é igual a {dados["MEDIA"]}')
print(f'situação é igual a {dados["SITUACAO"]}')