import random
import math
import time

lista = [[]]
nomes = []
i = 0
cont = 0

while (True):
    nome = str (input('Insira o nome: '))
    nota1 = float (input('Insira a primeira nota: '))
    nota2 = float (input('Insira a segunda nota: '))

    novoNome = [nome]
    novasNotas = [nota1,nota2,(nota1 + nota2) / 2]

    lista.append(novoNome[:])
    lista[0].append(novasNotas[:])

    i += 1
    cont += 1


    x = int (input('Deseja sair? [999]'))
    if (x == 999):
        break
        
for i in range (0,cont):
    print ('Numero {} /// Nome {} /// Média {}'.format(i,lista[i+1],lista[0][i][2]))

while (True):
    num = int (input('Mostrar notas de qual aluno?'))
    print('{} /// {}'.format(lista[0][num][0],lista[0][num][1]))

    escolha = int (input('Deseja sair?[999]'))
    if (escolha == 999):
        break


