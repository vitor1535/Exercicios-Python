import random
import math
import time

tupla = ('Lapis', 1.50, 'Caderno', 5.00, 'Livro', 25.00, 'Cadeira', 150.00)

for i in range (0,len(tupla) - 1, 2):
    print('{}........{}'.format(tupla[i],tupla[i+1]))