import random
import math

valor = int (input('Insira o valor da casa que quer comprar'))
salario = int (input('Insira o seu salario'))
anos = int (input('Insira em quantos anos voce que pagar'))

tempo = anos * 12
prestaçao = valor / tempo

if (prestaçao >= salario * 0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado! Valor da prestação = R${:.2f}'.format(prestaçao))