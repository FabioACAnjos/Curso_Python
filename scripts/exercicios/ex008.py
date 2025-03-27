#conversor de medidas - faça um programa e leia o valor em metros e exiba converstido em cm e mm

medida = float(input('Digite o comprimento em metros: '))

print('O valor em mm é {:.0f} mm' .format(medida*1000))
print('O valor em cm é {:.0f} cm' .format(medida*100))
