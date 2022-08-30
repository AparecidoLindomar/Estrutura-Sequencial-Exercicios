# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

genero = int(input('Digite 1 para homem ou 2 para mulher ? '))
altura = float(input('Informe sua altura ?'))

resultado_h = (72.7*altura)-58
resultado_m = (62.1*altura) - 44.7

if genero <= 1:
    print(f'Seu peso ideal é {resultado_h:.2f} kilos')
else:
    print(f'Seu peso ideal é {resultado_m:.2f} kilos')