# O mesmo professor do desafio anterior quer sortear a ordem de apresentção de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A sequencia para apresentação é: ')
print(lista)