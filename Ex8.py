# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


money_hora = float(input('Valor hora de trabalho ? '))
hora_mes = float(input('Horas trabalhadas mês ? '))

salario = money_hora * hora_mes

print (f'O seu salario este mês é {salario}.')