import random
import math
import time

primeiroTermo = int (input('Insira o primeiro termo'))
razao = int (input('Insira a razao'))

total = primeiroTermo

for i in range(0,10):
    total += razao

print('Valor total = {}'.format(total))