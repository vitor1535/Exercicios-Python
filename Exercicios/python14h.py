import random
import math
import time

n = 0
soma = 0
contador = 0

while (n != 999):
    n = int (input('Insira um valor'))
    soma = soma + n
    contador = contador + 1
    if (n == 999):
        soma = soma - 999
        contador = contador - 1

print('Soma total = {} /// Quantidade de numeros somados = {}'.format(soma,contador))