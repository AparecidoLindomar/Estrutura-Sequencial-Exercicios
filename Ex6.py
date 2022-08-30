# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

num = float(input('Digite o raio do circulo em m: '))
pi = math.pi
num2 = (num**2)

area = pi * num2

print(f'A área do raio do circulo é {area:.2f} m²')

