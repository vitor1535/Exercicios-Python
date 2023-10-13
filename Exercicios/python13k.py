import random
import math
import time

mediaIdade = 0
maiorIdade = 0
nomeMaisVelho = ''
contadorMulher = 0

for i in range(0,4):
    nome = str (input('Insira o nome'))
    idade = float (input('Insira a idade'))
    sexo = str (input('Insira o sexo[M/F]')).upper()

    mediaIdade += idade / 4

    if (idade > maiorIdade and sexo == 'M'):
        nomeMaisVelho = nome

    if (sexo == 'F' and idade < 20):
        contadorMulher += 1

print('Media de idade do grupo = {} \n Homem mais velho = {} \n Quantidade de mulheres com menos de 20 anos = {}'.format(mediaIdade,nomeMaisVelho,contadorMulher))
    