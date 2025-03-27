'''Escreva um programa que leia um numero inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''


num = int(input('Digite um valor para inicar seu fibonacci: '))
elementos = int(input('Quantos elementos você deseja saber? '))


c = 1
fibo = 0
f1 = 0
f2 = 1

print('{}'.format(f1), end= ' -> ')
print('{}'.format(f2), end= ' -> ')
while c <= elementos :
            
    fibo = f1 + f2
    print('{}'.format(fibo), end=' -> ')
    c += 1
    f1 = f2 
    f2 = fibo
            


print('Acabou')