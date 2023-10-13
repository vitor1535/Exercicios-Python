import random
import math

anoNascimento = int (input ('Insira o seu ano de nascimento'))

idade = 2023 - anoNascimento

if (idade < 18):
    print('Voce ainda vai se alistar, faltam {} anos!'.format(18 - idade))
elif (idade == 18):
    print('Voce precisa se alistar esse ano!')
elif (idade > 18):
    print('Ja passou do tempo de se alistar, voce está {} anos atrasados'.format(idade - 18))