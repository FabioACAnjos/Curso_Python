'''crie um programa que leia dois valores e mostre um meno na tela:
[1] para somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa'''

from time import sleep

valor1 = int(input('Digite o primeiro valor inteiro: '))
valor2 = int(input('Digite o segundo valor inteiro: '))
resultado = 0
maior = 0

sleep(0.4)
print('='*50)
print('Escolha uma das opções abaixo:')
print('[1] Somar os valores')
print('[2] Multiplicar os valores')
print('[3] Mostral qual é o maior valor')
print('[4] Escolher novos valores')
print('[5] Sair do programa')
print('='*50)
sleep(0.4)
escolha = int(input('Digite sua escolha: '))

if escolha == 5:
    print('Obrigado! Volte sempre!')
else:
    while escolha !=5:        
        if escolha == 1:
            sleep(0.4)
            resultado = valor1 + valor2
            print('Opção Escolhida Somar. \nO resultado da soma de {} com {} é igual à: {}' .format(valor1, valor2, resultado))
        elif escolha == 2:
            sleep(0.4)
            resultado = valor1 * valor2
            print('Opção Escolhida Multiplicar.\nO Resultado da multiplicação de {} com {} é igual à: {}' .format(valor1, valor2, resultado))
        elif escolha == 3:
            sleep(0.4)
            maior = valor1
            if maior < valor2:
                maior = valor2
                print('Opção Escolhida Maior Valor.\nO maior numero digitado foi {}' .format(maior))
            else:
                print('Opção Escolhida Maior Valor.\nO maior numero digitado foi {}' .format(maior))
        elif escolha == 4:
            sleep(0.4)
            valor1 = int(input('Digite primeiro novo valor: '))
            valor2 = int(input('Digite o segundo novo valor: '))
            
        sleep(0.6)
        print('='*50)
        print('Escolha uma das opções abaixo:')
        print('[1] Somar os valores')
        print('[2] Multiplicar os valores')
        print('[3] Mostral qual é o maior valor')
        print('[4] Escolher novos valores')
        print('[5] Sair do programa')
        print('='*50)
        sleep(0.4)
        escolha = int(input('Digite sua escolha: '))
        
        
    

    
    sleep(0.4)
    print('Obrigado! Volta Sempre!')