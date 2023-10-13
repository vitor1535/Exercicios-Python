import random
import math
import time

random = random.randint(0,10)
chute = 100
contagem = 0
    
while (chute != random):
    chute = int (input ('Chute um numero de 0 a 10 que o computador pensou!'))
    contagem = contagem + 1

print('Você acertou o numero {} com {} palpites!'.format(random,contagem))