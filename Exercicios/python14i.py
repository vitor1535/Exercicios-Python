import random
import math
import time

x = 'S'
maior = -1000
menor = 1000
soma = 0
contador = 0

while (x != 'n'):
    num = float(input('Insira um numero inteiro'))

    if(num < menor):
        menor = num
    if(num > maior):
        maior = num
    soma = soma + num

    contador = contador + 1

    x = str (input('Quer inserir mais valores? [S/N]')).lower()

media = soma / contador

print('Maior numero {} /// Menor numero = {} /// Media = {}'.format(maior,menor,media))