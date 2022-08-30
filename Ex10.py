# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.


tempera_celsi = float(input('Qual a temperatura °C ? '))

fahrenheit = ((tempera_celsi*9)/5)+32

print(f'A temperatura equivale a {fahrenheit:.2f}°F.')