# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lados = float(input('Digite o tamanho dos lados do quadrado: '))
area = lados * lados
dobro = area * 2
print(f'A area do quadrado e {area}, e o dobro dela e {dobro:.2f}')