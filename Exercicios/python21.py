import random
import math
import time

def voto(anoNascimento):
    if (2023 - anoNascimento < 18):
        resp = 'NEGADO!'

    elif (2023 - anoNascimento >= 18 and 2023 - anoNascimento < 65):
        resp = 'OBRIGATÓRIO'

    elif (2023 - anoNascimento > 65):
        resp = 'OPCIONAL'

    return resp

num = int (input('Insira sua idade: '))
resposta = voto(num)
print(resposta)