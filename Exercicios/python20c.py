import random
import math
import time

def contador(inicio, fim, passo):
    for i in range (1,11):
        print(i)
        time.sleep(0.2)

    for i in range(10,-1,-2):
        print(i)
        time.sleep(0.2)

    if (inicio > fim):
        if (passo > 0):
            passo = passo - passo - passo
            for i in range (inicio,fim-1,passo):
                print(i)
                time.sleep(0.2)   

        elif (passo < 0):
            for i in range (inicio,fim-1,passo):
                print(i)
                time.sleep(0.2)

        elif (passo == 0):
            passo = -1
            for i in range (inicio,fim-1,passo):
                print(i)
                time.sleep(0.2) 

    else:
        for i in range (inicio,fim+1,passo):
            print(i)
            time.sleep(0.2) 


x = int (input('Insira o inicio: '))
y = int (input('Insira o fim: '))
z = int (input('Insira o passo: '))

contador(x,y,z)