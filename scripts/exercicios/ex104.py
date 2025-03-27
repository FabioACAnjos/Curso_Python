#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt (numero):
    
    while True:
        numero = input('Digite um número: ')    
        if numero.isdigit():
            return numero
            break
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        
    




#PROGRAMA PRINCIPAL

n = leiaInt('Digite um numero: ')

print(f'Você acabou de digitar o numero {n}')