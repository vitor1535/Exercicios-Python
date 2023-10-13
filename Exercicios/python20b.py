import random
import math
import time

def escreva(texto):
    print('-' * (len(texto) + 4))
    print('  {}'.format(texto))
    print('-' * (len(texto) + 4))



x = str(input('Insira o texto: '))
escreva(x)