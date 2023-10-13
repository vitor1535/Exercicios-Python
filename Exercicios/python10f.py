import random
import math

num1 = int (input ('Insira o primeiro numero'))
num2 = int (input ('Insira o segundo numero'))
num3 = int (input ('Insira o terceiro numero'))

if (num1 > num2):
    maior = num1
    if(maior > num3):
        maior = num1
    else:
        maior = num3
else:
    maior = num2
    if(maior > num3):
        maior = num2
    else:
        maior = num3

if (num1 < num2):
    menor = num1
    if(menor < num3):
        menor = num1
    else:
        menor = num3
else:
    menor = num2
    if(menor < num3):
        menor = num2
    else:
        menor = num3

print('Maior numero = {} /// Menor numero = {}'.format(maior, menor))


