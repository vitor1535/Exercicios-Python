import random
import math

num1 = int (input ('Insira o primeiro numero'))
num2 = int (input ('Insira o segundo numero'))

if (num1 > num2):
    print ('O primeiro valor é maior')
elif (num1 < num2):
    print ('O segundo valor é maior')
else:
    print('Nao existe valor maior, os dois sao iguais')