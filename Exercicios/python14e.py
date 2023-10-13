import random
import math
import time

contador = 0

primeiroTermo = int (input('Insira o primeiro termo'))
razao = int (input('Insira a razão'))

termos = primeiroTermo 

print('{} - '.format(primeiroTermo))
while (contador < 9):
    termos = termos + razao
    print('{} - '.format(termos))   
    contador = contador + 1