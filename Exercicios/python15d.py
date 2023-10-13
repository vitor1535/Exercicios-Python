import random
import math
import time

num = 0
contador = 0
contadorIdade = 0
contadorHomem = 0
contadorMulher20 = 0


while (True):
    idade = int (input('Insira a idade'))
    sexo = str (input('Insira o sexo [M/F]')).upper()
    escolha = str (input('Quer continuar? [S/N]')).upper()

    if (idade > 18):
        contadorIdade += 1

    if (sexo == 'M'):
        contadorHomem += 1

    if (sexo == 'F' and idade < 20):
        contadorMulher20 += 1

    if (escolha == 'N'):
        break

print('Pessoas com mais de 18 anos = {}'.format(contadorIdade))
print('Homens cadastrados = {}'.format(contadorHomem))
print('Mulheres com menos de 20 anos = {}'.format(contadorMulher20))