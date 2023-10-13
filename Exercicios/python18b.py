import random
import math
import time

lista = [[],[]]


for i in range (0,7):
    num = int (input('Insira um numero'))

    if (num % 2 == 0):
        lista[0].append(num)

    if (num % 2 == 1):
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(lista)
