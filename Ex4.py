# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

b1 = float(input("Digite a note do 1° Bimestre:"))
b2 = float(input("Digite a note do 2° Bimestre:"))
b3 = float(input("Digite a note do 3° Bimestre:"))
b4 = float(input("Digite a note do 4° Bimestre:"))
media = b1 + b2 + b3 + b4
mediafinal = media / 4

print(f'A média final do aluno é:',mediafinal)