import random
import math
import time

num = int (input('Escolha um numero para a tabuada'))

for i in range(1,11):
    print('{} x {} = {}'.format(num, i, num * i))
