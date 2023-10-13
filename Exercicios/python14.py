import random
import math
import time

sexo = 'F'
sexo = str (input ('Insira o sexo [M/F]')).upper()

while (sexo != 'F' and sexo != 'M'):
    print('Valor incorreto, digite novamente!')
    sexo = str (input ('Insira o sexo [M/F]')).upper()
    