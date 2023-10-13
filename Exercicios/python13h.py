import random
import math
import time

contador = 0

frase = str (input('Insira uma frase')).strip()
palavrasSeparadas = frase.split()
junto = ''.join(palavrasSeparadas)
frase = junto

for i in range(0,len(frase)):
    if(frase[i] == frase[len(frase) - i - 1]):
        contador = contador + 1 

if (contador == len(frase)):
    print('É palindromo!')
else:
    print('Nao é palíndromo!')