"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""
qtd_horas = int(input('Quanto ganha por hora? '))
horas_trabalhadas = int(input('Horas trabalhadas por mês: '))

salario_bruto = qtd_horas * horas_trabalhadas
ir = salario_bruto * 0.11
inss= salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print(f'Salario bruto R$ : {salario_bruto:.2f}')
print(f'IR R$: {ir:.2f}')
print(f'INSS R$: {inss:.2f}')
print(f'Sindicato R$: {sindicato:.2f}')
print(f'Salario Liquido R$: {salario_liquido:.2f}')