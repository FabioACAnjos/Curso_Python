#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = {
    'NOME':'',
    'ANO': 0,
    'CARTEIRA': 0
}

dados['NOME'] = str(input('Nome: '))
dados['ANO'] = int(input('Ano de Nascimento: '))
dados['CARTEIRA'] = int(input('Carteira de Trabalho (0 não tem): '))
idade = datetime.now().year - dados['ANO']
dados['IDADE'] = idade

if dados['CARTEIRA'] != 0:
    dados['CONTRATACAO'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Salário: '))
    ano_apostadoria = dados['CONTRATACAO'] + 35
    idade_aposentaroria = ano_apostadoria - dados['ANO']
    dados['IDADE_APOSENTADORIA'] = idade_aposentaroria



print('=-' *20)

for k , v in dados.items():
    print(f'{k} tem o valor: {v}')