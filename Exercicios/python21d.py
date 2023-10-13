import random
import math
import time

def leiaInt(n):
    if (n.isnumeric()):
        print('{} é numero!'.format(n))
    else:
        while (True):
            print('{} não é numero!'.format(n))
            n = str(input('Digite novamente.'))

            if (n.isnumeric()):
                print('{} é numero!'.format(n))
                break



teste = str(input('Insira algo: '))
leiaInt(teste)



