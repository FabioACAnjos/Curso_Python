#desevolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Primeira nota do Aluno: '))
n2 = float(input('Segunda nota do Aluno: '))

m = (n1+n2)/2

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}' .format(n1, n2, m))