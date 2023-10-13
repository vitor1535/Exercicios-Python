import random
import math
import time
from pacoteMoeda import modDados
from pacoteMoeda import mod112

p = str(input('Digite algo: '))
p = mod112.leiaDinheiro(p)
modDados.resumo(p, 80, 30)