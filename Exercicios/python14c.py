import random
import math
import time

escolha = 10

num1 = int (input('Insira o primeiro valor'))
num2 = int (input('Insira o segundo valor'))

print(' [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos numeros \n [5] Sair \n')

while (escolha != 5):

    escolha = int (input('Escolha uma opção!'))

    if (escolha == 1):
        resultado = num1 + num2
        print('Resultado = {}'.format(resultado))
    elif (escolha == 2): 
        resultado = num1 * num2
        print('Resultado = {}'.format(resultado))           
    elif (escolha == 3):
        if(num1 > num2):
            print('Maior = {}'.format(num1))
        elif(num1 < num2):
            print('Maior = {}'.format(num2))
        else:
            print('Os dois numeros sao iguais!')
    elif (escolha == 4):
        num1 = int (input('Insira o primeiro valor'))
        num2 = int (input('Insira o segundo valor'))