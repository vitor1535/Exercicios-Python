import random
import math
import time

dicionario = {}
lista = []
media = 0
contMulher = 0
contAcimaMedia = 0

while (True):
    nome = str (input('Insira o nome: '))
    sexo = str (input('Insira o sexo [M/F]')).upper()
    idade = int (input('Insira a idade: '))

    dicionario = {
                    'nome' : nome,
                    'sexo' : sexo,
                    'idade' :idade 
                 }
    
    lista.append(dicionario.copy())

    x = str (input('Deseja continuar? [S/N]')).upper()
    if (x == 'N'):
        break

for i in range (0,len(lista)):
    media += lista[i]['idade'] / len(lista)   

    if (lista[i]['sexo'] == 'F'):
        contMulher += 1

for i in range (0,len(lista)):
    if (lista[i]['idade'] > media):
        contAcimaMedia += 1

print('{} pessoas foram cadastradas.'.format(len (lista)))
print('{} é a media de idade'.format(media))
print('{} são mulheres.'.format(contMulher))
print('{} tem a idade acima da média.'.format(contAcimaMedia))