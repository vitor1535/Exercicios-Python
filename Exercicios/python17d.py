import random
import math
import time

vetor = []
contador = 0
contador5 = 0

while (True):
    num = int (input('Insira um numero'))
    vetor.append(num)

    contador += 1

    if (num == 5):
        contador5 += 1

    if (num == 999):
        vetor.pop()
        contador -= 1
        break

print('Numeros digitado = {}'.format(contador))

vetor.sort(reverse = True)
print(vetor)

if (contador5 == 0):
    print('Valor 5 nao foi digitado')
else:
    print('Valor 5 foi digitado {} vezes'.format(contador5))