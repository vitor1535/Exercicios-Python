import random
import math
import time

vetor = []
listaPar = []
listaImpar = []

while (True):
    num = int (input('Insira um numero'))

    if (num == 999):
        break
    else:
        vetor.append(num)

for i in range (0,len(vetor)):
    if (vetor[i] % 2 == 0):
        listaPar.append(vetor[i])
    elif (vetor[i] % 2 == 1):
        listaImpar.append(vetor[i])

print('Todos os numeros = {}'.format(vetor))
print('Pares = {}'.format(listaPar))
print('Impares = {}'.format(listaImpar))