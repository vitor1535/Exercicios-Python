import random
import math

escolha = int (input('Escolha uma base numerica (1 - binario / 2 - octal / 3 - hexadecimal)'))
num = int (input('Qual numero?'))

if (escolha == 1):
    print (bin(num))
elif (escolha == 2):
    print (oct(num))
elif (escolha == 3):
    print (hex(num))