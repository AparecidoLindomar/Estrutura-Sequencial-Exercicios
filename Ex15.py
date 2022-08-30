# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#  sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a.salário bruto.
# b.quanto pagou ao INSS.
# c.quanto pagou ao sindicato.
# d.o salário líquido.

# e.calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

money_hora = float(input('Valor por hora trabalhada ? '))
hora_mes = float(input('Horas trabalhadas mês ? '))
salario_bruto = money_hora * hora_mes
imposto_renda = (salario_bruto/100)*11
inss = (salario_bruto/100)*8
sindicato = (salario_bruto/100)*5
imposto = imposto_renda + inss + sindicato
salario_liquido = salario_bruto - imposto

print(f'inss R$ {inss:.2f}')
print(f'salario bruto R$ {salario_bruto:.2f}')
print(f'sindicato R$ {sindicato:.2f}')
print(f'imposto de renda R$ {imposto_renda:.2f}')
print(f'Seu salário liquido este mês é R${salario_liquido:.2f}.')

