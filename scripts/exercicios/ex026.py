# Faça um programa que leia uma frase pelo teclado e mostre: 
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparace a última vez.


frase = str(input('Digite uma frase: ')).upper().strip()

print('Essa frase contem {}x a letra "A"' .format(frase.count('A')))

print('A primeira letra "A" está na posição {}' .format(frase.find('A')+1))

print('A última letra "A" aparece na posição {}' .format(frase.rfind('A')+1))