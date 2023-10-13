import random
import math
import time

soma = 0
contador1000 = 0
barato = 999999

while (True):
    produto = str (input('Insira o produto'))
    preço = int (input('Insira o preço do produto'))
    escolha = str (input('Quer continuar? [S/N]')).upper()

    soma += preço

    if (preço > 1000):
        contador1000 += 1

    if (preço < barato):
        barato = preço

    if (escolha == 'N'):
        break

print('Total gasto = {} /// Produtos a mais de R$1000 = {} /// Produto mais barato = {}'.format(soma,contador1000,barato))