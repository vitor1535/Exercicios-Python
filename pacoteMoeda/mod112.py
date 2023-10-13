import random
import math
import time

def leiaDinheiro (n = ''):
    while (True):
        if (n.isnumeric()):
            n = float (n)
            return n

        else:
            n = str (input('Digite um numero'))

