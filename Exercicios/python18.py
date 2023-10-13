import random
import math
import time

lista = []
cont = 0
listaPesado = []
listaLeve = []
resposta = 'S'
pesado = 0
leve = 999


while (True):
    nome = str (input('Insira o nome: '))
    peso = int (input('Insira o peso: '))

    lista.append(nome)
    lista.append(peso)
   
    cont += 1

    resposta = str (input('Quer continuar? [S/N]')).upper()

    if (resposta == 'N'):
        break

for i in range (0,len(lista) - 1, 2):
    if (lista[i+1] > pesado):
        pesado = lista[i+1]
    
    if (lista[i+1] < leve):
        leve = lista[i+1]
    
for i in range(0,len(lista) - 1, 2):
    if (lista[i+1] == pesado):
        listaPesado.append(lista[i])
        listaPesado.append(lista[i+1])

    if (lista[i+1] == leve):
        listaLeve.append(lista[i])
        listaLeve.append(lista[i+1])

print('{} pessoas foram cadastradas'.format(cont))
print('{} foram as pessoas mais pesadas'.format(listaPesado))
print('{} foram as pessoas mais leves'.format(listaLeve))
