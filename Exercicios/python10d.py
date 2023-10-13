import random
import math

num = int (input ('Qual a distancia em km?'))

if (num <= 200):
    preço = 0.50 * num
else:
    preço = 0.45 * num

print('Preço total = {}'.format(preço))



