import random
import math
import time

total = 0
contador = 0

for i in range(1,501):
    if(i % 3 == 0 and i % 2 == 1):
        total = total + i
        contador = contador + 1

print('Valor total da soma = {} / Quantidade de numeros = {}'.format(total,contador))