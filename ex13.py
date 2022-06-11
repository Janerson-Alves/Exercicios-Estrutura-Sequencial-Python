"""
Tendo como dado de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*altura) - 58
Para mulheres: (62.1*altura) - 44.7
"""
sexo = input('Você e [1] Homem [2] Mulher? ')
altura = float(input('Digite a sua altura: '))

if sexo == '1':
    peso = (71.7 * altura) - 58
    print(f'Você e homem e seu peso ideal e {peso}kg')
elif sexo == '2':
    peso = (62.1 * altura) - 44.7
    print(f'Você e mulher e seu peso ideal e {peso}kg')
else:
    print('Sexo invalido!')