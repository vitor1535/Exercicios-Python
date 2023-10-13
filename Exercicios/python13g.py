import random
import math
import time

contador = 0

num = int(input('Insira um numero'))

for i in range(1,num+1):
    if(num % i == 0):
        contador = contador + 1

if (contador == 2):
    print('Numero primo!')
else:
    print('Nao é primo!')