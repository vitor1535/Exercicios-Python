import random
import math
import time
import webbrowser

def menu ():
    print('---------------------------')
    print('1 - Ver lista')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair')
    print('---------------------------')

def verLista():
    a = open('python23d.txt', 'rt')

    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n','')
        print('{} - {}'.format(dado[0],dado[1]))

    a.close()


lista = []

while (True):

    menu()
    opç = int (input('Insira uma opção: '))

    if (opç == 1):
        verLista()

    if (opç == 2):
        nome = str(input('Insira o nome: '))
        idade = int(input('Insira a idade: '))

        a = open('python23d.txt', 'at+')
        a.write('{};{} \n'.format(nome,idade))
        a.close()

    if (opç == 3):
        break


