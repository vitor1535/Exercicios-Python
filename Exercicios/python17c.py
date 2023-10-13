import random
import math
import time

vetor = []

for i in range (0,5):
    num = int (input('Insira um numero '))

    if (i == 0):
        vetor.append(num)
    else:
        for j in range (0, len(vetor)):
            if (num < vetor[j]):
                vetor.insert(j,num)
                break
            elif (j == len(vetor) - 1):
                vetor.append(num)

print(vetor)

