# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = int(input('Digite o primeiro número ?'))
num2 = int(input('Digite o segundo número ?'))
num3 = float(input('Digite o terceiro número ?'))

resultado_a = num1*2 + num2/2
resultado_b = num1*3 +num3
resultado_c = num3**3


print(f'O valor do dobro do primeiro com metade do segundo é {resultado_a:.0f}')
print(f'O valor da soma do triplo do primeiro com o terceiro  {resultado_b:.0f}')
print(f'O valor ao cudo do terceiro número é {resultado_c:.0f}')