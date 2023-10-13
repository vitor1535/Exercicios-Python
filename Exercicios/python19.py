import random
import math
import time

nome = str (input('Insira o nome: '))
media = int (input('Insira a media'))

if (media >= 7):
    situação = 'Aprovado'
else:
    situação = 'Reprovado'

dicionario = {'nome' :nome, 'media': media, 'situação': situação}

print('O nome = {}'.format(dicionario['nome']))
print('A media = {}'.format(dicionario['media']))
print('A situaçao = {}'.format(dicionario['situação']))