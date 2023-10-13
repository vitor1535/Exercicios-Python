import random
import math
import time

dicionario = {}

nome = str (input('Insira o nome: '))
anoNascimento = int(input('Insira o ano de nascimento: '))
clt = int(input('Insira a clt: '))

if (clt == 0):
    dicionario = {'nome': nome,
                  'idade': 2023 - anoNascimento,
                  'clt': clt}
    
    print(dicionario.items())

else:
    anoContratação = int (input('Insira o ano de contratação: '))
    salario = int (input('Insira o salário: '))

    dicionario = {'nome': nome,
                  'idade': 2023 - anoNascimento,
                  'clt': clt,
                  'anoContratação': anoContratação,
                  'salario': salario,
                  'aposentadoria': 2023 - anoNascimento + (35 - (2023 - anoContratação))}
    
    print(dicionario['nome'])
    print(dicionario['aposentadoria'])