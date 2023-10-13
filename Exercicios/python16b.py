import random
import math
import time

x = 0

extenso = ('um','dois','tres','quatro','cinco','seis','chapecoense','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while (True):

    print('[1] - Exibir os 5 primeiros')
    print('[2] - Exibir os 4 ultimos')
    print('[3] - Exibir times em ordem alfabetica')
    print('[4] - Exibir posição do chapeconse')
    print('[5] - Sair')

    x = int (input('Escolha uma opção!'))

    if (x == 1):
        print('{}'.format(extenso[:5]))

    if (x == 2):
        print('{}'.format(extenso[16:]))

    if (x == 3):
        print('{}'.format(sorted(extenso)))

    if (x == 4):     
        print('Chapecoense na posição {}'.format(extenso.index('chapecoense') + 1))

    if (x == 5):
        break
        