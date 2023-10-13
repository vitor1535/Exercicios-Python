import random
import math

velocidade = int (input ('Escolha a velocidade do carro.'))
multa = math.floor((velocidade - 80) / 10)

if (velocidade > 80):
    print('Voce foi multado! Valor de R${}'.format(multa))
else:
    print('Voce nao foi multado!')





