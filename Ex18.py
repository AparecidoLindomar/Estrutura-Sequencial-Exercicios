# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).



mb = float(input("Qual o tamanho do arquivos em MB ? "))
velocidade = float(input('Qual a velocidade da sua internet em Mbps ?'))

download = mb / velocidade


print(f'Este aquivo vai demorar {download:.2f} segundo para fazer o downaload')