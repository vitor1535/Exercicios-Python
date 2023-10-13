import random
import math
import time

def ficha (nome = '<desconhecido>', gols = 0):
    print('O jogador {} fez {} gols!'.format(nome,gols))



string = str(input('Insira o nome do jogador: '))
int = str(input('Insira os gols: '))

if (string == ''):
    string = '<desconhecido>'

if (int == ''):
    int = 0

ficha(string,int)

