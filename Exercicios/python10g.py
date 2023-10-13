import random
import math

salario = int (input ('Insira o salario'))

if (salario > 1250):
    resultado = salario * 1.10
else:
    resultado = salario * 1.15

print('Salario pos aumento = {}'.format(resultado))