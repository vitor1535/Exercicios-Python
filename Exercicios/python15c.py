import random
import math
import time

num = 0
soma = 0
contador = 0
vitorias = 0

while (True):
    jogador = int (input('Escolha um numero'))
    computador = random.randint(0,10)

    escolha = str (input('Par ou impar? [P/I]')).upper()

    resultado = jogador + computador
    if (resultado % 2 == 0):
        total = 'P'
    else:
        total = 'I'

    print('Você jogou {} e a maquina jogou {}! Total = {}'.format(jogador,computador,resultado))

    if (escolha == total):
        print('Você ganhou!')
        vitorias += 1
    else:
        print('Você perdeu!')
        print('{} vitorias consecutivas!'.format(vitorias))
        break