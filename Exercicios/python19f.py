import random
import math
import time

dicionario = {}
lista = []
soma = 0
tudo = []

while (True):
    lista = []
    soma = 0

    nome = str(input('Insira o nome: '))
    quantidadePartidas = int (input('Insira a quantidade de partidas: '))

    for i in range(0, quantidadePartidas):
        gols = int (input('Quantos gols fez na partida {}?'.format(i+1)))
        lista.append(gols)

    for i in range (0,quantidadePartidas):
        soma += lista[i]

    dicionario  = {
                'nome': nome,
                'quantidade de partidas': quantidadePartidas,
                'gols': lista,
                'golsTotal': soma
                }
    
    tudo.append(dicionario.copy())
    
    x = int (input('Digite 999 para sair.'))
    if (x == 999):
        break

for i in range (0,len(tudo)):
    print('{} - {} -------- {} ----- {}'.format(i,tudo[i]['nome'],tudo[i]['gols'],tudo[i]['golsTotal']))

while (True):

    escolha = int (input('Mostrar dados de qual jogador?'))

    if (escolha != 999):
        print('-- Levantamento do jogador'.format(tudo[escolha]['nome']))
        for i in range(0,len (tudo[escolha]['gols'])):
            print('No jogo {} fez {} gols.'.format(i,tudo[escolha]['gols'][i]))

    else:
        print('Programa finalizado!')
        break
