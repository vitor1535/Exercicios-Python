import random
import math
import time

def leiaInt():
    try:
        numero = int (input('Insira um numero: '))

    except:
        while (True):
            numero = str (input('Digite apenas numero: '))

            if (numero.isnumeric()):
                break
    
    return numero

def leiaFloat():
    while (True):
        try:
            numero = float (input('Insira um numero: '))
            return numero

        except KeyboardInterrupt:
            print('O usuario nao quis digitar!')
            numero = 0
            return numero

        except:        
            print('Digite apenas numero!')


n = leiaInt()
f = leiaFloat()
print(n,f)
