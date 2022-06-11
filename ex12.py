"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal
usando a seguinte fórmula: (72.7*altura) - 58
"""

altura = float(input('Digite sua altura: '))
peso = (72.7 * altura) - 58
print(f'O Peso ideal para a altura {altura} e de {peso:.2f} kg ')