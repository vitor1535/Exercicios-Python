import random
import math
import time

vetor = []
maior = 0
menor = 9999
posicaoMenor = 0
posicaoMaior = 0

for i in range (0,5):
    vetor.append(int (input('Insira o valor da posiçao {}'.format(i))))
    
    if (vetor[i] > maior):
        maior = vetor[i]
        posicaoMaior = i

    if (vetor[i] < menor):
        menor = vetor[i]
        posicaoMenor = i

for i in range (0,len(vetor)):
    print('{}'.format(vetor[i]))

print('Menor valor = {} / Posição {}'.format(menor, posicaoMenor))
print('Maior valor = {} / Posição {}'.format(maior, posicaoMaior))