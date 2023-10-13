import random
import math
import time

contador = 0

n = int (input ('Insira quantos termos da sequencia de fibonacci deseja'))

primeiroTermo = 0
segundoTermo = 1

print(primeiroTermo)
print(segundoTermo)

while(contador < n - 2):
    proximo = primeiroTermo + segundoTermo
    primeiroTermo = segundoTermo
    segundoTermo = proximo
    print('{}'.format(proximo))
    contador = contador + 1