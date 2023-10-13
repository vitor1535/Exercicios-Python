import random
import math
import time

def maior(num):
    maior = -999

    for i in range(0,len(num)):
        if (num[i] > maior):
            maior = num[i]

    print('Maior numero da lista é o {}'.format(maior))

lista = []

while (True):
    num = int (input('Insira um numero: '))

    lista.append(num)
    print(lista)

    opc = str (input('Deseja continuar? [S/N]')).upper()
    if (opc == 'N'):
        break
teste = lista
maior(teste)
