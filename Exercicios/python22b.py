import random
import math
import time
from pacoteMoeda import modMoeda

resultado1 = modMoeda.dobrar(100)
resultado2 = modMoeda.moeda(modMoeda.metade(100))
resultado3 = modMoeda.moeda(modMoeda.aumentar(100, 10))
resultado4 = modMoeda.moeda(modMoeda.diminuir(100, 10))

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)