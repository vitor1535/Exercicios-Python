import random
import math
import time

cont9 = 0
pares = 0

num1 = int (input('Insira um numero'))
num2 = int (input('Insira um numero'))
num3 = int (input('Insira um numero'))
num4 = int (input('Insira um numero'))

tupla = (num1,num2,num3,num4)

for i in range (0,len(tupla)):
    
    if (tupla[i] % 2 == 0):
        pares += 1

cont9 = tupla.count(9)

if (3 in tupla):
    respB = tupla.index(3)
else:
    respB = 'Nao existe'

print('9 aparece {} vezes, 3 apareceu na posição {} e tiveram {} numeros pares!'.format(cont9,respB,pares))