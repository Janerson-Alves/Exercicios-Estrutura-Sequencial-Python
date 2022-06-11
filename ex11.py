"""
“Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.”
"""
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

produto = n1 * 2 * (n2 / 2)
soma = n1 * 3 + n3
terceiro = n3 ** 3

print(f'dobro do primeiro com metade do segundo e {produto}')
print(f'a soma do triplo do primeiro com o terceiro e {soma}')
print(f'o terceiro elevado ao cubo e {terceiro:.2f}')

