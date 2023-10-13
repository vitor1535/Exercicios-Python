import random
import math
import time

matriz = []

n = int (input('Quantos jogos serao criados?'))

for i in range (0,n):
    novoJogo = [random.randint(1,60), random.randint(1,60), random.randint(1,60), random.randint(1,60), random.randint(1,60), random.randint(1,60)]
    matriz.append(novoJogo[:]) 

print(matriz)