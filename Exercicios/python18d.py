import random
import math
import time

matriz = [[],[],[]]
soma = 0
somaColuna = 0
maiorLinha = 0

for i in range (0,3):
    for j in range (0,3):
        num = int (input('Insira um numero: '))
        matriz[i].append(num)

for i in range (0,3):
    for j in range (0,1):
        print(matriz[i][j], matriz[i][j+1], matriz[i][j+2])

for i in range (0,3):
    for j in range (0,3):
        if (matriz[i][j] % 2 == 0):
            soma += matriz[i][j]

        if (j == 2):
            somaColuna += matriz[i][j]

        if (i == 1):
            if (matriz[i][j] > maiorLinha):
                maiorLinha = matriz[i][j]

print('A) Soma de todos os valores = {}'.format(soma))
print('B) Soma de todos os valores da terceira coluna = {}'.format(somaColuna))
print('C) Maior valor da segunda linha = {}'.format(maiorLinha))