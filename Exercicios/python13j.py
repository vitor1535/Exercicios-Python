import random
import math
import time

maior = 0
menor = 1000

for i in range(0,5):
    peso = int (input('Insira o peso'))
    if (peso > maior):
        maior = peso
    elif (peso < menor):
        menor = peso

print('O maior peso foi {}kg e o menor foi {}kg'.format(maior,menor))