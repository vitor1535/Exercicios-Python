import random
import math
import time

def ajuda (str):
    help(str)


while (True):
    comando = str (input('Insira o comando: '))
    if (comando == 'FIM'):
        break
    else:
        ajuda(comando)