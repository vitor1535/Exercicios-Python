import random
import math
import time

numero = []

def sorteia():
    for i in range (0,5):
        numero.append(random.randint(0,100))
    
    print(numero)


def somaPar(num):
    soma = 0
    for i in range (0, len(num)):
        if (num[i] % 2 == 0):
            soma += num[i]

    print(soma)

sorteia()
somaPar(numero)


