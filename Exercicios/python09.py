import random

nome = str (input ('Insira o seu nome completo'))
qtdLetras = len(nome) - (nome.count(' '))
nomeDividido = nome.split()

print('Em maisculo = {}'.format(nome.upper()))
print('Em minusculo = {}'.format(nome.lower()))
print('Quantidade de letras = {}'.format(qtdLetras))
print('Primeiro nome = {}'.format(nomeDividido[0]))





