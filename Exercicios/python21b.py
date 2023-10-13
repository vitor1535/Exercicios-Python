import random
import math
import time

def fatorial(n,show = False):
    if (show == False):
        resultado = 1
        while (n != 0):
            resultado *= n
            n = n - 1

        print (resultado)
    
    elif(show == True):
        resultado = 1
        aux = n
        while (n != 0):
            resultado *= n
            n = n - 1

        for aux in range (aux, 0, -1):
            print('{} '.format(aux),end= "")
            if (aux != 1):
                print('x'.format(aux),end= " ")
            else:
                print('='.format(aux),end= " ")
        print('{}'.format(resultado))

    return resultado


retorno = fatorial(5,show = True)
print(retorno)