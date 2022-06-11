#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
tf = float(input('Digite a quantidade de Graus em Fahrenheit: '))
tc = 5*((tf-32)/9)
print(f"A temperatura em Graus celsius e de {tc:.2f}")