import random
import math
import time

def notas(* num, sit = False):
    """
    Explicação: Pode colocar quantos numeros quiser que retornará um dicionário.
    Comando sit: opcional, caso deseje mostra tambem a situaçao da turma.
    """
    media = 0
    print(num)

    for i in range (0, len(num)):
        if (i == 0):
            maior = num[i]
            menor = num [i]

        else:
            if (num[i] > maior):
                maior = num[i]

            if (num[i] < menor):
                menor = num[i]

        media += num[i] / len (num)

        if (media >= 7):
            situação = 'Boa'
        elif (media >=5 and media < 7):
            situação = 'Media'
        elif (media < 5):
            situação = 'Ruim'

    if (sit == False):
        dicionario = {'Quantidade' : len(num),
                      'Maior' : maior,
                      'Menor' : menor,
                      'Média' : media}
            
    elif (sit == True):
        dicionario = {'Quantidade' : len(num),
                      'Maior' : maior,
                      'Menor' : menor,
                      'Média' : media,
                      'Situação' : situação}
            
    return dicionario


resultado = notas(3.5, 2, 6.5, sit = True)
help(notas)
print(resultado)