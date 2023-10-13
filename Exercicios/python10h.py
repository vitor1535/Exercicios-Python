import random
import math

reta1 = int (input('Insira a primeira reta do triangulo'))
reta2 = int (input('Insira a segunda reta do triangulo'))
reta3 = int (input('Insira a terceira reta do triangulo'))

if (reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2):
    print('Pode formar triangulo')
else:
    print('Nao pode formar um triangulo')