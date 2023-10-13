import random
import math
import time

tupla = ('riven', 'yasuo', 'zed', 'kaisa', 'jhin', 'ezreal', 'talyah')

vogalA = 0
vogalE = 0
vogalI = 0
vogalO = 0
vogalU = 0

for i in range(0, len(tupla)):
    for j in range (0,len(tupla[i])):
        if (tupla[i][j].lower() == 'a'):
            vogalA = 1

        elif (tupla[i][j].lower() == 'e'):
            vogalE = 1

        elif (tupla[i][j].lower() == 'i'):
            vogalI = 1

        elif (tupla[i][j].lower() == 'o'):
            vogalO = 1

        elif (tupla[i][j].lower() == 'u'):
            vogalU = 1

    print('Qtd de A = {} / Qtd de E = {} / Qtd de I = {} / Qtd de O = {} / Qtd de U = {}'.format(vogalA, vogalE, vogalI, vogalO, vogalU))

    vogalA = 0
    vogalE = 0
    vogalI = 0
    vogalO = 0
    vogalU = 0
            