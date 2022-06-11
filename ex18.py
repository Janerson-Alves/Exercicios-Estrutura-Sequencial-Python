"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
tamanhoArquivo = float(input("Digite o tamanho do arquivo para download: "))
velocidade = float(input("Digite a velocidade de um link de internet: "))
segundos = tamanhoArquivo/velocidade
minutos = int(segundos / 60)
segundos = segundos % 60
print("Tempo aproximado para download: " , (minutos) ," minutos e " , str(segundos) , " segundos")