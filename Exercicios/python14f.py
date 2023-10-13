import random
import math
import time

contador = 0
maisTermos = 100

primeiroTermo = int (input('Insira o primeiro termo'))
razao = int (input('Insira a razão'))

resultado = primeiroTermo 

print('{} - '.format(primeiroTermo))

while (contador < 9):
    resultado = resultado + razao
    print('{} - '.format(resultado))   
    contador = contador + 1

while (maisTermos != 0):
    contador2 = 0
    maisTermos = int (input('Voce quer ver mais quantos termos?'))

    while (contador2 < maisTermos):
        resultado = resultado + razao
        print('{} - '.format(resultado))   
        contador2 = contador2 + 1
                



