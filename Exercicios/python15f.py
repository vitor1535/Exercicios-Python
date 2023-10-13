import random
import math
import time

contador50 = 0
contador20 = 0
contador10 = 0
contador1 = 0

saque = int (input('Insira o valor a ser sacado: '))

while (saque - 50 >= 0):
    saque = saque - 50
    contador50 += 1

while (saque - 20 >= 0):
    saque = saque - 20
    contador20 += 1

while (saque - 10 >= 0):
    saque = saque - 10
    contador10 += 1

while (saque - 1 >= 0):
    saque = saque - 1
    contador1 += 1

print('Serão entres {} cédulas de 50, {} cédulas de 20, {} cédulas de 10 e {} cédulas de 1,'.format(contador50,contador20,contador10,contador1))