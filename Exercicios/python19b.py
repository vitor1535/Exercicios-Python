import random
import math
import time

dicionario = []
maior = 1
aux = 0

num1 = random.randint(1,6)
num2 = random.randint(1,6)
num3 = random.randint(1,6)
num4 = random.randint(1,6)

dicionario.append(num1)
dicionario.append(num2)
dicionario.append(num3)
dicionario.append(num4)

for i in range (0,3):
    for j in range (0,3):
        if (dicionario[j] > dicionario[j + 1]):
            aux = dicionario[j]
            dicionario[j] = dicionario[j+1]
            dicionario[j+1] = aux

for i in range (0,4):
    print(dicionario[i])

print('O vencedor tirou o dado {}'.format(dicionario[3]))