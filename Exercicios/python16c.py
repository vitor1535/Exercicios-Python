import random
import math
import time

menor = 100
maior = 0

num1 = random.randint(0,10)
num2 = random.randint(0,10)
num3 = random.randint(0,10)
num4 = random.randint(0,10)
num5 = random.randint(0,10)

tupla = (num1, num2, num3, num4, num5)

print(tupla)

for i in range(0,len(tupla)):

    if (tupla[i] > maior):
        maior = tupla[i]

    if (tupla[i] < menor):
        menor = tupla[i]

print('Maior valor = {} /// Menor valor = {}'.format(maior,menor))