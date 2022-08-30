#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#           °C = 5 * ((°F-32) / 9).

tempera_fahre = float(input('Qual a temperatura °F'))

celsius = ((tempera_fahre - 32)*5)/9

print(f'A temperatura equivale a {celsius:.2f}°C.')
