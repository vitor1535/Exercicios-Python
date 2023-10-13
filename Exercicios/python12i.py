import random
import math

valor = int (input ('Insira o valor do produto'))
tipoPagamento = int (input('1 - Dinheiro / 2 - Cheque / 3 - Cartão'))

if (tipoPagamento == 1):
    print('Valor com 10% de desconto! Valor total = R${}'.format(valor * 0.90))
elif (tipoPagamento == 2):
    print('Valor com 10% de desconto! Valor total = R${}'.format(valor * 0.90))
elif (tipoPagamento == 3):
    parcelas = int (input('Parcelado em quantas vezes?'))
    if (parcelas == 1):
        print('Valor com 5% de desconto! Valor total = R${}'.format(valor * 0.95))
    elif (parcelas == 2):
        print('Valor com 0% de desconto! Valor total = R${}'.format(valor))
    elif (parcelas >= 3):
        print('Valor com 20% de juros! Valor total = R${}'.format(valor * 1.20))