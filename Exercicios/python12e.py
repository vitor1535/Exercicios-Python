import random
import math

nota1 = int (input ('Insira a primeira nota'))
nota2 = int (input ('Insira a segunda nota'))

media = (nota1 + nota2) / 2

if (media < 5):
    print('Reprovado!')
elif (media >= 5 and media <= 6.9):
    print ('Recuperação!')
elif (media >= 7):
    print ('Aprovado!')
