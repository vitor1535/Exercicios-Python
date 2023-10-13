import random
import math
import time

dicionario = {}
lista = []
soma = 0

nome = str(input('Insira o nome: '))
quantidadePartidas = int (input('Insira a quantidade de partidas: '))

for i in range(0, quantidadePartidas):
    gols = int (input('Quantos gols fez na partidas {}?'.format(i+1)))
    lista.append(gols)

for i in range (0,quantidadePartidas):
    soma += lista[i]

dicionario  = {
               'nome': nome,
               'quantidade de partidas': quantidadePartidas,
               'gols': lista,
               'golsTotal': soma
               }


print(dicionario.items())

print('------------------------------')

print('O campo nome tem o valor {}'.format(dicionario['nome']))
print('O campo gols tem o valor {}'.format(dicionario['gols']))
print('O campo total tem o valor {}'.format(dicionario['golsTotal']))

print('------------------------------')

print('O jogador {} jogou {} partidas.'.format(dicionario['nome'],dicionario['quantidade de partidas']))
for i in range(0,5):
    print('Na partida {}, fez {} gols.'.format(i, lista[i]))
print('Foi um total de {} gols.'.format(dicionario['golsTotal']))