import random
import math
import time

num = int (input ('Insira um numero'))

auxiliar = num - 1
resultado = num

while (auxiliar != 1):
    resultado = resultado * auxiliar
    auxiliar = auxiliar - 1

print('Fatorial de {} = {}'.format(num, resultado))