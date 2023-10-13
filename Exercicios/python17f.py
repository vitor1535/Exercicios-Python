import random
import math
import time

vetor = []
contadorP1 = 0
contadorP2 = 0
resultado = 0

expressao = str (input('Insira a expressao'))

for i in range (0, len (expressao)):
    if (expressao[i] == '('):
        contadorP1 += 1
        resultado += contadorP1

    elif (expressao[i] == ')'):
        contadorP2 -= 1
        resultado += contadorP2

        if (resultado < 0):
            print('Expressão invalida!')
            break

    

if (contadorP1 + contadorP2 == 0):
    print('Expressão valida!')


