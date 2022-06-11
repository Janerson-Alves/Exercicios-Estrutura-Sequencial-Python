"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
qtd_horas = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = float(input('Horas trabalhadas no mês: '))

salario_bruto = qtd_horas * horas_trabalhadas

print(f'O salario é {salario_bruto:.2f} por mês')