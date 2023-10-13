import random
import math
import time

num = 0
soma = 0
contador = 0

while (True):
    num = int (input('Insira um numero'))
    if(num == 999):
        break
    else:
        soma += num
        contador += 1

print('Total = {} e foram digitados ao todos {} numeros.'.format(soma, contador))