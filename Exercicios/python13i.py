import random
import math
import time

contador = 0

for i in range(0,7):
    anoNascimento = int (input('Insira o ano de nascimento da pessoa {}'.format(i + 1)))
    if (2023 - anoNascimento >= 18):
        contador += 1

print('Quantidade de pessoas que ja atingiram a maioridade = {}'.format(contador))