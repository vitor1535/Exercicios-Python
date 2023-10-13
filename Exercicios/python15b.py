import random
import math
import time

num = 0
soma = 0
contador = 0

while (True):
    num = int (input('Insira o numero para a tabuada'))
    if (num < 0):
        break
    else:
        for i in range (1,11):
            print('{} x {} = {}'.format(num,i,num * i))