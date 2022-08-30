# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math

area = float(input("Informe a área a ser pintada em m²?"))
valor_lata = 80
litro_tinta = 18 

litro = area / 3

qtd_latas2 = (litro / litro_tinta)

qtd_latas = math.ceil(qtd_latas2)

preço_total = qtd_latas * valor_lata

print(f'area {area:.2f}')
print(f'litro {litro:.2f}')
print(f'quantidade de latas {qtd_latas2:.2f}')

print(f'Vamos utilizar {qtd_latas:.2f} e o valor total é R${preço_total:.2f}')